from tsp_ga import tsp_ga
from cromossomo import cromossomo 
from boxplot import boxplot

if __name__ == '__main__':
    execucoes = 1
    somaDist = 0
    melhorCrom = cromossomo.cromVazio()
    melhoresDist = []
    for i in range(execucoes):
        melhorCrom = tsp_ga.main(tamPopulacao=100, nPais=25, geracoes=20, p=0.005)[0]
        somaDist += melhorCrom.getDistTotal()
        melhoresDist.append(melhorCrom.getDistTotal())
    distTotalMedia = somaDist/execucoes

    boxplot(melhoresDist)
    print(distTotalMedia)
    
