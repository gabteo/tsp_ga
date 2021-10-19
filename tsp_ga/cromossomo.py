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
        for i in range(len(apelidoCidades)):
            self.gene.append(apelidoCidades[i])
        random.shuffle(self.gene)
        self.calculafitness()
        

    # no argumento, seria melhor passar matriz de distancias ou 
    # instancia da classe cidades? Onde mapear nome da cidade para
    # índice da matriz?
    def calculafitness(self):
        # Origem: linhas
        # Destino: colunas
        matriz = self.objCidades.getMatrizDist()
        self.distTotal = 0
        self.fitness = 0
        apelidos = self.objCidades.getApelidos()
        for i in range(len(self.gene)-1):
            #quando retorna ao inicio:
            #indexOrigem = np.where(apelidos == self.gene[i-1])
            #indexDestino = np.where(apelidos == self.gene[i])

            #quando não retorna ao inicio
            indexOrigem = np.where(apelidos == self.gene[i-1])
            indexDestino = np.where(apelidos == self.gene[i])
            # soma as distancias e torna o total negativo
            self.distTotal += (matriz[indexOrigem,indexDestino])
            # self.fitness=self.fitness+(matriz[self.gene[i],self.gene[i+1]])
        
        self.fitness = self.distTotal*(-1)
        numVertices = len(apelidos)
        
        # vamos encontrar o total de arestas, se o grafo fosse completo, e... 
        # funciona, mas talvez não seja a melhor ideia. Ver outra opção no próx bloco de comentario.
        # self.fitness += self.objCidades.getMaxDist()*(numVertices/2)*(numVertices-1)

        # somamos ao fitness (negativo) um valor certamente maior que qquer fitness possível,
        # que é o fit de uma rota em que todas as distâncias são iguais à dist máxima
        self.fitness += self.objCidades.getMaxDist()*numVertices
        # agora fitness é positivo, e valores maiores representam rotas menores
        # print("fitness=" + str(self.fitness))
            
    def setProbSel(self, fitTot):
        self.probSel = self.fitness/fitTot

    def getProbSel(self):
        return self.probSel


    #por troca
    # implementar probabilidade de realizar mutacao
    def mutacaoEM(self):
        i=random.randrange(len(self.gene)-1)
        j=random.randrange(len(self.gene)-1)
        while (i==j):
            j=random.randrange(len(self.gene))
        self.gene[i],self.gene[j]=self.gene[j],self.gene[i]
        # recalcula fitness após mutação:
        self.calculafitness()


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

    def getDistTotal(self):
        return self.distTotal
            