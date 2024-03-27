{{
    config(
        materialized='view'
    )
}}

WITH victimas_data AS 
(
  SELECT *
  FROM {{ source('staging', 'victims_cdmx') }}
  WHERE alcaldia_hecho IS NOT NULL
)
SELECT
    categoria_delito AS crime_category,
    delito AS crime,
    {{ fill_type_person("tipo_persona") }} AS person_type,
    {{ fill_legal_quality("calidad_juridica") }} AS legal_quality,
    {{ fill_scope("competencia") }} AS scope,
    {{ fill_townhall_fact("alcaldia_hecho") }} AS townhall_fact,
    {{ fill_town_fact("municipio_hecho") }} AS town_fact,
    hecho_date AS fact_date
FROM victimas_data
{% if var('is_test_run', default=true) %}

  LIMIT 100

{% endif %}