import pandas as pd


def get_pandas_data():
    mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
    }
    return pd.DataFrame(mydataset)
