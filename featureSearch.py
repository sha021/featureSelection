import stdScale as std
import numpy as np
from sklearn.preprocessing import normalize

def featureSearch(dataSet):
    NUM_FEAT = np.size(dataSet, 1)
    selectedSet = []
    for i in range(1, NUM_FEAT):
        toAdd = []
        accuracy = 0
        print("On the " + str(i) + "th level of the search tree")
        #for j in range(1, NUM_FEAT):
            #if k not in selectedSet:
            #    printf("--- Considering adding the feature " + str(k))
                

a = np.loadtxt('cs_170_small34.txt')
#dataSet = np.array(normalize(a, axis=0, norm='max')) 
dataSet = np.array(a)
normedSet = std.stdScale(dataSet)
with np.printoptions(threshold=np.inf):
    print(normedSet)
    #np.save('normedfile', data)
featureSearch(normedSet)

 