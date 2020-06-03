from stdScale import stdScale
from leaveOneOut import leaveOneOut as validation

def featureSearch(dataSet):
    NUM_FEAT = len(dataSet.columns)
    bestAccuracy = 0
    maxOfLevel = []
    selectedSet = []
    for i in range(1, NUM_FEAT):
        toAdd = []
        maxAccuracy = 0
        feat = 0
        print("     On the " + str(i) + "th level of the search tree")
        for j in range(1, NUM_FEAT):
            if j not in maxOfLevel:
                accuracy = validation(dataSet, selectedSet, j)
                if (accuracy > maxAccuracy):
                    maxAccuracy = accuracy
                    feat = j
                print("          Using feature " + str(j) + ", accuracy is " + str(accuracy))
        if (feat not in maxOfLevel): maxOfLevel.append(feat)
        if (maxAccuracy > bestAccuracy):
            bestAccuracy = maxAccuracy
            selectedSet.append(feat)
            print("the feature set ", selectedSet, "is the best, accuracy is  ", bestAccuracy)
        else: 
            print("(((Warning, Accuracy has decreased! Continuing search in case of local maxima)))")
            print("the feature set ", maxOfLevel, "is the best, accuracy is  ", maxAccuracy)
    print("Finished search! the best feature subset is ", selectedSet, " which has an accuracy of ", bestAccuracy)
dataSet = stdScale()
featureSearch(dataSet)



 