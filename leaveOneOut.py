import pandas as pd
import nn
def leaveOneOut(dataSet, selectedSet, feature):
    NUM_ITEM = len(dataSet)
    distSet = []
    top = 0
    bottom = NUM_ITEM
    # sortedSet = dataSet.sort_values(feature)
    # col = pd.Series(sortedSet[feature])
    for i in range(NUM_ITEM):
        top = top + nn.nearNeighbor(dataSet, selectedSet, feature, i)
    return (top/bottom)
    
    