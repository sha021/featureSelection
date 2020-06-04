from stdScale import greeting
from leaveOneOut import leaveOneOut as validation

def featureSearch(dataSet):
    NUM_FEAT = len(dataSet.columns)
    bestAccuracy = 0
    maxOfLevel = []
    selectedSet = []
    classSet = dataSet[0]
    for i in range(1, NUM_FEAT):
        maxAccuracy = 0
        feat = 0
        print("     On the " + str(i) + "th level of the search tree")
        for j in range(1, NUM_FEAT):
            consider = []
            for chosen in maxOfLevel:
                consider.append(chosen)
            if j not in maxOfLevel:
                consider.append(j)
                choppedSet = dataSet[consider]
                accuracy = validation(classSet, choppedSet)
                if (accuracy > maxAccuracy):
                    maxAccuracy = accuracy
                    feat = j               
                print("\tUsing feature " + str(consider) + ", accuracy is " + str(accuracy))
        if (feat not in maxOfLevel): 
            maxOfLevel.append(feat)
        if (maxAccuracy <= bestAccuracy):
            print("(((Warning, Accuracy has decreased! Continuing search in case of local maxima)))")
        else:
            bestAccuracy = maxAccuracy
            selectedSet.append(feat)
        print("the feature set ", maxOfLevel, "is the best, accuracy is  ", maxAccuracy)
    print("Finished search! the best feature subset is ", selectedSet, " which has an accuracy of ", bestAccuracy)


def main():
    dataSet = greeting()
    classSet = dataSet[0]
    chopped = dataSet[1:]
    print("Running nearest neighbor with all", (len(dataSet.columns) - 1), "feature(s), using \"leaving-one-out\" evaluation, I get an accuracy of ", validation(classSet, chopped))
    featureSearch(dataSet)

if __name__ == "__main__":
    main()