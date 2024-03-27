{{ config(materialized='table') }}

WITH victimas_data AS (
    SELECT * FROM {{ ref('stg_victims_cdmx') }}
)
SELECT
    townhall_fact,
    crime,
    EXTRACT(YEAR FROM fact_date) AS year,
    COUNT(1) AS total
FROM victimas_data
GROUP BY 1, 2, 3
ORDER BY total DESC