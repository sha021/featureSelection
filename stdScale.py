import pandas as pd

def stdScale(data):
    for col in range(1, len(data.columns)):
        data[col] = (data[col] - data[col].mean())/data[col].std()
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(data)  
    return data

def greeting():
    print("Welcome to Seung Eun Ha Feature Selection Algorithm.")
    filename = input("Type in the name of the file to test: ")
    data = pd.read_csv(filename, header=None, sep=r"\s+")
    print("The dataset has ", (len(data.columns) - 1), "features (NOT including the class attribute), with ", (len(data)), "instances. ")
    print("Please wait while I normalize the data...... Done!")
    dataSet = stdScale(data)
    print("*****Let's use Forward Selection*****")
    return dataSet
