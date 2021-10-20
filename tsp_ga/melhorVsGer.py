import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

def melhorVsGer(geracoes, distMin):
    xint = range(0, geracoes+2)
    plt.xticks(xint)
    geracao = []
    #geracao = np.array([])
    for i in range(geracoes+2):
        geracao.append(i)
    #dist = np.array(distMin)
    dist = distMin
    plt.title('Distância Mínima vs. geração')
    plt.xlabel('Geração')
    plt.ylabel('Dist. mínima')
    plt.plot(geracao,dist)
    fig = plt.figure(figsize=(10, 7))
    #plt.clf()
    plt.show()

