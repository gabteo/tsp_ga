import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

def boxplot(lista):
    lst = np.array(lista)
    #stddeviation = np.std(lst)
    #mean = np.mean(lst)
    data = lst.flatten()

    fig = plt.figure(figsize=(10, 7))
    plt.boxplot(data, vert=False)
    plt.show()

