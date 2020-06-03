def nearNeighbor(dataSet, selectedSet, feature, item):
    NUM_ITEM = len(dataSet)
    col = dataSet[feature]
    classSet = dataSet[0]
    minDist = 99999
    cur = col[item]
    predict = 0
    for row in range(1, NUM_ITEM):
        if row != item :
            dist = 0
            #selected distances
            if (len(selectedSet) > 0):
                for chosen in selectedSet:
                    column = dataSet[chosen]
                    dist = dist + (column[item] - column[row]) ** 2
            #new feature distance
            dist = dist + (cur - col[row]) ** 2
            if (dist < minDist):
                minDist = dist
                predict = row
    return (classSet[predict] == classSet[item])