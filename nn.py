import math 

def nearNeighbor( item, choppedSet):
    NUM_ITEM = len(choppedSet)
    minDist = 99999
    predict = 0
    test = choppedSet.iloc[item]    
    for row in range(1, NUM_ITEM):
        if row == item: 
            continue
        train = choppedSet.iloc[row]
        dist = math.sqrt(sum([(a-b) ** 2 for a, b in zip(test, train)]))
        if (dist < minDist):
            minDist = dist
            predict = row
    return predict
