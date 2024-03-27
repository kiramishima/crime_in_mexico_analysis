-- Create an external table from
CREATE OR REPLACE EXTERNAL TABLE `bq_victims_cdmx.external_victims_cdmx`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://victims-cdmx-bucket/*.parquet']
);

-- Create a table from external table
-- Also add the partition and clustering
CREATE OR REPLACE TABLE bq_victims_cdmx.victims_cdmx
PARTITION BY
    hecho_date
CLUSTER BY categoria_delito, delito, alcaldia_hecho AS
SELECT * FROM bq_victims_cdmx.external_victims_cdmx
WHERE EXTRACT(YEAR from hecho_date) >= 2019;