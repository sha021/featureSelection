import stdScale as std
import numpy as np
from sklearn.preprocessing import normalize

def featureSearch(data):
    selected = [];
    for i in range(1, np.size(data, 1)):
        print("On the " + str(i) + "th level of the search tree")

a = np.loadtxt('cs_170_small34.txt')
data = np.array(normalize(a, axis=0, norm='max')) 
std.stdScale(data)
featureSearch(data)

