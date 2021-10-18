import csv
import numpy as np
# lembrar: pip install numpy

#matrix=np.random.randint(2,10,(4,4))
#np.fill_diagonal(matrix,0)

class cidades(object):
    def __init__(self):
        self.carregarCidades()

    def carregarCidades(self):
        #str é "gambiarra" para formatar vetor do numpy
        str = "str"

        # abre os arquivos de nome da US, endereco e tabela de dist
        self.arquivoDists = open("tsp_ga\\dist.csv")
        self.enderecos = open("tsp_ga\\enderecos.txt")
        self.us = open("tsp_ga\\US.txt")

        # Cria matriz e vetores a partir dos arquivos
        self.enderecosVetor = np.loadtxt(self.enderecos, dtype = type(str), delimiter=";")
        self.usVetor = np.loadtxt(self.us, dtype = type(str), delimiter=";")
        self.matrizDist = np.loadtxt(self.arquivoDists, delimiter=";")

        # Origem: linhas
        # Destino: colunas

        self.maxDist = self.matrizDist.max()
        
        print(self.matrizDist)
        print(self.usVetor)
        # print(self.enderecosVetor)

    # retorna vetor de apelidos das "cidades", no caso o nome das US
    def getApelidos(self):
        return self.usVetor

    def getEnderecos(self):
        return self.enderecosVetor

    def getMatrizDist(self):
        return self.matrizDist

    def getMaxDist(self):
        return self.maxDist


# teste: instancia classe, imprime vetores e matriz
#dists = CidadesDados()