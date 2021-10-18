import tsp_ga
from cidades import cidades
from cromossomo import cromossomo
import crossover
import random

def main():
    print("HELLLO do tsp_ga")
    tamPopulacao = 10
    #unidadesSaude = cidades()

    pop = geraPopInicial(tamPopulacao)
    
    # imprime populacoes geradas
    for i in range(len(pop)):
        print("---cromossomo " + str(i)+":")
        for j in range(len(pop[i])):
            cr = pop[i]
            print(cr[j])
        print("---fitness=" + str(pop[i].getFitness()))
        print("\n")
    
    p=0.01
    mutacao(p,pop)

def geraPopInicial(tamPopulacao):
    popInicial = []
    for i in range(tamPopulacao):
        novoCromossomo = cromossomo.cromFromFile()
        #novoCromossomo = cromossomo.cromossomoFromObjCidades(unidadesSaude)
        popInicial.append(novoCromossomo)
    return popInicial

def chance(p):
    return random.random()<p


def mutacao(p,pop):

    for i in range(len(pop)):
        if chance(p):
            print("Gene antigo "+ str(pop[i].gene))
            pop[i].mutacaoEM()
            print("Gene novo " + str(pop[i].gene))

