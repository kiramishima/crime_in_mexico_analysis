import pandas as pd
from pandas import DataFrame
from time import time

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs) -> DataFrame:
    list_data = []
    for year in range(2019, 2024):
        t_start = time()
        url = f"https://archivo.datos.cdmx.gob.mx/FGJ/victimas/victimasFGJ_{year}.csv"
        print("Reading: ", url)
        victimas_dtypes = {
            'age': pd.Int64Dtype()
        }

        df = pd.read_csv(url, sep=',', dtype=victimas_dtypes)
        print(df.shape)
        list_data.append(df)
        t_end = time()
        print('process time, took %.3f second' % (t_end - t_start))

    t_start = time()
    df_concat = pd.concat(list_data, ignore_index=True)
    t_end = time()
    print(df_concat.shape)
    print('concat time, took %.3f second' % (t_end - t_start))
    return df_concat

