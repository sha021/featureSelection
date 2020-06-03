import pandas as pd
# def leaveOneOut(dataSet, selectedSet, nextFeature):
#     NUM_ITEM = np.size(dataSet, 0)
    
#     for i in range(NUM_ITEM):
#         copySet[0]
data = pd.read_csv("cs_170_small34.txt", header=None, sep=r"\s+")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data)
