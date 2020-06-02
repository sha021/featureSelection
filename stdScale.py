from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
#import pandas as pd
import numpy as np
from scipy import stats

# def stdScale():
#     token = open('cs_170_small34.txt','r')
#     linestoken=token.readlines()
#     tokens_column_number = 1
#     f1=[]
#     for x in linestoken:
#         resulttoken.append(x.split()[tokens_column_number])
#     token.close()
#     print(resulttoken)

def stdScale():
    # whole file
    a = np.loadtxt('cs_170_small34.txt')
    data = np.array(normalize(a, axis=0, norm='max'))
    #print(np.size(data, 0))
 
    for row in range(np.size(data, 0)):
        data[row, 0] = data[row, 0] * 2 

    with np.printoptions(threshold=np.inf):
        print(data)
        np.save('normedfile', data)
        
stdScale()

