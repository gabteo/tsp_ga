from typing import Optional
import tsp_ga
from cidades import cidades
from cromossomo import cromossomo
from crossover import crossover
import random
import time
from melhorVsGer import melhorVsGer 

def main(tamPopulacao = 100, nPais = 20, geracoes = 20, p = 0.002):
    start_time = time.time()
    #tamPopulacao = 1000 #1200 1000
    # numero de pais selecionados para cruzamento em cada geracao:
    #nPais = 40 #25 40
    #geracoes = 30
    #Probabilidade de Mutação
    #p=0.002

    crossoverObj = crossover()
    fitTot = 0
    
    # armazena cromossomos da população inicial gerada em lista
    pop = geraPopInicial(tamPopulacao)
    geracaoAtual = 0
    vetDistMin = []
    vetDistMin.append(getMelhorDist(pop, tamPopulacao))
    
    
    for m in range(geracoes): 
        geracaoAtual = m
        
        # calcula fitTot e imprime populacoes geradas
        for i in range(len(pop)):
            fitTot += pop[i].getFitness()
            #impressão dos cromossomos:
            imprimeCrom = False

            if imprimeCrom:
                print("---cromossomo " + str(i)+":")
                for j in range(len(pop[i])):
                    cr = pop[i]
                    print(cr[j])
                print("---fitness=" + str(pop[i].getFitness()))
                print("---distTot=" + str(pop[i].getDistTotal()))
                print("\n")

        # calcula a probabilidade de seleção    
        for i in range(len(pop)):
            for j in range(len(pop[i])):
                pop[i].setProbSel(fitTot)

        # seleciona pais para cruzamento
        pais = roleta(pop, nPais)
        
        # realiza cruzamento e adiciona filhos à população
        pop = cruzamento(pop, pais, crossoverObj)     
        #Aplica a probabilidade de mutação a todos os integrantes da população
        mutacao(p,pop)

        vetDistMin.append(getMelhorDist(pop, tamPopulacao))

        # remove piores cromossomos até que len(pop) = tamPopulacao
        pop = selecionaPop(pop, tamPopulacao)
        fitTot = 0
        
    melhorCrom = selecionaPop(pop, 1)
    for i in range(len(melhorCrom)):
        print("---cromossomo " + str(i)+":")
        for j in range(len(melhorCrom[i])):
            cr = melhorCrom[i]
            print(cr[j])        
        print("---Melhor fitness=", int(melhorCrom[i].getFitness()))
        print("---Menor distTot=", int(melhorCrom[i].getDistTotal()), "m")
    
    print("TEMPO: ",(time.time()-start_time))
    vetDistMin.append(getMelhorDist(pop, tamPopulacao))
    melhorVsGer(geracoes, vetDistMin)
    return melhorCrom
    



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
    return populacao

def selecionaPop(pop, tamPopulacao):
    fitList = []
    #print(len(pop))
    if len(pop) > tamPopulacao:
        for i in range(len(pop)):
            fitList.append(pop[i].getFitness())
    
    while len(pop) > (tamPopulacao):
        minFit = min(fitList)
        indexMinFit = fitList.index(minFit)
        del pop[indexMinFit]
        del fitList[indexMinFit]
    return pop

def getMelhorDist(pop, tamPopulacao):
    dists = []
    for i in range(len(pop)):
        dists.append(pop[i].getDistTotal()[0][0])
    return min(dists)

def mutacao(p,pop):
    for i in range(len(pop)):
        if (random.random()<p):
            #print("Gene antigo "+ str(pop[i].gene))
            pop[i].mutacaoEM()
            pop[i].calculafitness()
            #print("Gene novo " + str(pop[i].gene))
