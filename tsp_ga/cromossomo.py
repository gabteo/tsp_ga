import random
from collections import Sequence
from cidades import cidades
import numpy as np

class cromossomo(object):
    #gene = []
    #fitness=0
    objCidades = cidades()

    def __init__(self, apelidoCidades, size):
        self.gene = []
        self.fitness=0
        for i in range(len(apelidoCidades)):
            self.gene.append(apelidoCidades[i])
        random.shuffle(self.gene)
        self.calculafitness(self.objCidades.getMatrizDist())
        

    # no argumento, seria melhor passar matriz de distancias ou 
    # instancia da classe cidades? Onde mapear nome da cidade para
    # índice da matriz?
    def calculafitness(self, matriz):
        # Origem: linhas
        # Destino: colunas
        apelidos = self.objCidades.getApelidos()
        for i in range(len(self.gene)-1):
            indexOrigem = np.where(apelidos == self.gene[i-1])
            indexDestino = np.where(apelidos == self.gene[i])
            self.fitness += (matriz[indexOrigem,indexDestino])
            # self.fitness=self.fitness+(matriz[self.gene[i],self.gene[i+1]])
        print("fitness=" + str(self.fitness))
            
        
    #por troca
    # implementar probabilidade de realizar mutacao
    def mutacaoEM(self):
        i=random.randrange(len(self.gene)-1)
        j=random.randrange(len(self.gene)-1)
        while (i==j):
            j=random.randrange(len(self.gene))

        self.gene[i],self.gene[j]=self.gene[j],self.gene[i]


    @classmethod
    def cromFromSize(cls, size):
        cls.cidadesVazio = []
        for i in range(size):
            cls.cidadesVazio.append('')
        return cls(cls.cidadesVazio, size)

    @classmethod
    def cromFromCidades(cls, Cidades):
        return cls(Cidades, len(Cidades))

    @classmethod
    def cromFromObjCidades(cls, objCid):
        cls.objCidades = objCid
        apelidos = objCid.getApelido()
        return cls(apelidos, len(apelidos))

    @classmethod
    def cromFromFile(cls):
        apelidos = cls.objCidades.getApelidos()
        return cls(apelidos, len(apelidos))

    @classmethod
    def cromVazio(cls):
        return cls([],0)
        
    def append(self, item):
        self.gene.append(item)
    
    def __getitem__(self, i):
        return self.gene[i]
    def __len__(self):
        return len(self.gene)
    def __setitem__(self, key, value):
        self.gene[key] = value
    def __str__(self):
        self.str = str(self.gene)
        return self.str

    def getFitness(self):
        return self.fitness
            