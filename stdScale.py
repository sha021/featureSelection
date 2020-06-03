import pandas as pd

def stdScale():
    data = pd.read_csv("cs_170_small34.txt", header=None, sep=r"\s+")
    for col in range(1, len(data.columns)):
        data[col] = (data[col] - data[col].mean())/data[col].std()
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(data)  
    return data
