from stdScale import stdScale
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
def plots():
    data = stdScale()
    # threedee = plt.figure().gca(projection='3d')
    # threedee.scatter(data[5], data[3], data[7])
    # threedee.set_xlabel('5')
    # threedee.set_ylabel('3')
    # threedee.set_zlabel('7')
    
    fig, ax = plt.subplots()
    colors = []

    colors = data[0]
    x = data[:2,3]
    y = data[:4,5]
    plt.scatter(x,y,marker='o',c = colors)
    plt.show()
plots()