import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def main(params):
    # DB Connection
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(f'./{csv_name}', iterator=True, chunksize=100000, low_memory=False)

    # iterate chunk by chunk
    while True:
        try:
            t_start = time()
            df = next(df_iter)
            # Filter fecha and hora nulls
            df = df[(df.fecha_inicio.notnull()) & (df.hora_inicio.notnull())]
            # Create new column datetime
            # Create datetime: dt_inicio
            df['dt_inicio'] = df[(df.fecha_inicio.notnull()) & (df.hora_inicio.notnull())][['fecha_inicio', 'hora_inicio']] \
                .apply(lambda row: datetime.strptime(f"{row.fecha_inicio} {row.hora_inicio}", "%Y-%m-%d %H:%M:%S"), axis=1)
            # Create datetime: dt_hecho
            df['dt_hecho'] = df[(df.fecha_hecho.notnull()) & (df.hora_hecho.notnull())][['fecha_hecho', 'hora_hecho']] \
                .apply(lambda row: datetime.strptime(f"{row.fecha_hecho} {row.hora_hecho}", "%Y-%m-%d %H:%M:%S"), axis=1)
            # Fill NAN values with 'No especifico'
            df['delito'].fillna('No especifico', inplace=True)
            df['categoria_delito'].fillna('No especifico', inplace=True)
            df['sexo'].fillna('No especifico', inplace=True)
            df['tipo_persona'].fillna('No especifico', inplace=True)
            df['calidad_juridica'].fillna('No especifico', inplace=True)
            df['competencia'].fillna('No especifico', inplace=True)
            df['colonia_hecho'].fillna('No especifico', inplace=True)
            df['colonia_catalogo'].fillna('No especifico', inplace=True)
            df['alcaldia_hecho'].fillna('No especifico', inplace=True)
            df['alcaldia_catalogo'].fillna('No especifico', inplace=True)
            df['municipio_hecho'].fillna('No especifico', inplace=True)
            # Drop date columns & latlong
            df.drop(columns=['anio_inicio', 'mes_inicio', 'fecha_inicio', 'hora_inicio', 'anio_hecho', 'mes_hecho', 'fecha_hecho', 'hora_hecho', 'latitud', 'longitud'], inplace=True)
            # 
            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)