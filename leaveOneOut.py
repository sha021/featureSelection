from nn import nearNeighbor

def leaveOneOut(classSet, choppedSet):
    NUM_ITEM = len(choppedSet)
    top = 0

    for i in range(NUM_ITEM):
        predict = nearNeighbor(i, choppedSet)
        if (classSet[predict] == classSet[i]) :
            top += 1
    return (top/NUM_ITEM)
    