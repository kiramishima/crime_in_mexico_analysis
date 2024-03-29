{{
    config(
        materialized='view'
    )
}}

WITH victimas_data AS 
(
  SELECT *,
  ROW_NUMBER() OVER(PARTITION BY categoria_delito, delito, hecho_datetime, inicio_datetime) as rn
  FROM {{ source('staging', 'victims_cdmx') }}
  WHERE alcaldia_hecho IS NOT NULL
)
SELECT
    -- identifiers
    {{ dbt_utils.generate_surrogate_key(['categoria_delito', 'delito', 'hecho_datetime', 'inicio_datetime']) }} as crime_id,
    categoria_delito AS crime_category,
    delito AS crime,
    {{ fill_type_person("tipo_persona") }} AS person_type,
    {{ fill_legal_quality("calidad_juridica") }} AS legal_quality,
    {{ fill_scope("competencia") }} AS scope,
    {{ fill_townhall_fact("alcaldia_hecho") }} AS townhall_fact,
    {{ fill_town_fact("municipio_hecho") }} AS town_fact,
    -- date
    hecho_date AS fact_date,
    inicio_date AS register_date,
    -- timestamps
    TIMESTAMP_MICROS(CAST(hecho_datetime / 1000 AS INT64)) as fact_datetime,
    TIMESTAMP_MICROS(CAST(inicio_datetime / 1000 AS INT64)) as register_datetime,
FROM victimas_data
WHERE rn = 1
{% if var('is_test_run', default=true) %}

  LIMIT 100

{% endif %}