import tsp_ga
from cidades import cidades
from cromossomo import cromossomo
from crossover import crossover
import random

def main():
    tamPopulacao = 100
    #unidadesSaude = cidades()
    fitTot = 0
    crossoverObj = crossover()
    
    # numero de pais selecionados para cruzamento em cada geracao:
    nPais = 50
    geracoes = 20
    # armazena cromossomos da população inicial gerada em lista
    pop = geraPopInicial(tamPopulacao)
    geracaoAtual = 0
    
    for m in range(geracoes): 
        # calcula fitTot e imprime populacoes geradas
        for i in range(len(pop)):
            #print("---cromossomo " + str(i)+":")
            for j in range(len(pop[i])):
                cr = pop[i]
                #print(cr[j])
            fitTot += pop[i].getFitness()
            
            #print("---fitness=" + str(pop[i].getFitness()))
            #print("---distTot=" + str(pop[i].getDistTotal()))
            #print("\n")

        # calcula a probabilidade de seleção    
        for i in range(len(pop)):
            for j in range(len(pop[i])):
                pop[i].setProbSel(fitTot)

        # seleciona pais para cruzamento
        pais = roleta(pop, nPais)
        print("geravao: " + str(geracaoAtual))
        geracaoAtual += 1
        # realiza cruzamento e adiciona filhos à população
        pop = cruzamento(pop, pais, crossoverObj)

        # remove piores cromossomos até que len(pop) = tamPopulacao
        pop = selecionaPop(pop, tamPopulacao)

        fitTot = 0
        
    
    melhorCrom = selecionaPop(pop, 1)
    for i in range(len(melhorCrom)):
        print("---cromossomo " + str(i)+":")
        for j in range(len(melhorCrom[i])):
            cr = melhorCrom[i]
            print(cr[j])        
        print("---Melhor fitness=" + str(melhorCrom[i].getFitness()))
        print("---Menor distTot=" + str(melhorCrom[i].getDistTotal()))
            

    



def geraPopInicial(tamPopulacao):
    popInicial = []
    for i in range(tamPopulacao):
        novoCromossomo = cromossomo.cromFromFile()
        #novoCromossomo = cromossomo.cromossomoFromObjCidades(unidadesSaude)
        popInicial.append(novoCromossomo)
    return popInicial

def roleta(populacao, qtdSelec):
    pais = []
    for j in range(qtdSelec):
        i = 0
        soma = populacao[i].getProbSel()
        # arrumar pra [0,1], ao inves de [0,1)
        r = random.uniform(0.0, 1.0)
        while soma < r:
            i += 1
            soma += populacao[i].getProbSel()
        pais.append(populacao[i])
    return pais

def cruzamento(populacao, pais, crossoverObj):
    #essa primeira linha tá certa?
    filhos = []
    qtdPais = len(pais)
    for i in range(qtdPais):
        for j in range(qtdPais):
            if i is not j:
                populacao.extend(crossoverObj.ox(pais[i], pais[j]))
                #filhos = crossoverObj.ox(pais[i], pais[j])
                #print(type(filhos))
                #for n in range(len(filhos)):
                #    populacao.append(filhos[n])
    return populacao

def selecionaPop(pop, tamPopulacao):
    fitList = []
    print(len(pop))
    if len(pop) > tamPopulacao:
        for i in range(len(pop)):
            fitList.append(pop[i].getFitness())
    
    while len(pop) > (tamPopulacao):
        minFit = min(fitList)
        indexMinFit = fitList.index(minFit)
        del pop[indexMinFit]
        del fitList[indexMinFit]
    return pop

    #popSort = 
    #while len(pop) > tamPopulacao:
    #    pop.remove(min(pop, key = pop.))
    # criar cls pop com cromossomo e fit????