from pandas import DataFrame
from time import time
from datetime import datetime

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data: DataFrame, *args, **kwargs) -> DataFrame:
    print(data.shape)
    print(data.columns)
    t_start = time()
    # Filter fecha and hora nulls
    df = data[(data.fecha_inicio.notnull()) & (data.hora_inicio.notnull())]
    # Create datetime: dt_inicio
    df['inicio_datetime'] = df[(df.fecha_inicio.notnull()) & (df.hora_inicio.notnull())][['fecha_inicio', 'hora_inicio']] \
        .apply(lambda row: datetime.strptime(f"{row.fecha_inicio} {row.hora_inicio}", "%Y-%m-%d %H:%M:%S"), axis=1)
    # Create datetime: dt_hecho
    df['hecho_datetime'] = df[(df.fecha_hecho.notnull()) & (df.hora_hecho.notnull())][['fecha_hecho', 'hora_hecho']] \
        .apply(lambda row: datetime.strptime(f"{row.fecha_hecho} {row.hora_hecho}", "%Y-%m-%d %H:%M:%S"), axis=1)
    
    # Create a new column hecho_date by converting hecho_datetime to a date.
    df['hecho_date'] = df['hecho_datetime'].dt.date
    # Create a new column inicio_date by converting inicio_datetime to a date.
    df['inicio_date'] = df['inicio_datetime'].dt.date

    # Drop date columns & latlong
    df.drop(columns=['anio_inicio', 'mes_inicio', 'fecha_inicio', 'hora_inicio', 'anio_hecho', 'mes_hecho', 'fecha_hecho', 'hora_hecho', 'latitud', 'longitud'], inplace=True)
    t_end = time()
    print(df.shape)
    print('transform time, took %.3f second' % (t_end - t_start))
    return df[df.notnull()]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
