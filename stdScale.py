from sklearn.preprocessing import normalize
#import pandas as pd
import numpy as np
from scipy import stats

def stdScale(data):
    for row in range(np.size(data, 0)):
        data[row, 0] = data[row, 0] * 2 

    with np.printoptions(threshold=np.inf):
        print(data)
        np.save('normedfile', data)

a = np.loadtxt('cs_170_small34.txt')
data = np.array(normalize(a, axis=0, norm='max')) 
stdScale(data)

