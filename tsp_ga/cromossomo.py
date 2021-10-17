
from collections import Sequence
import cidades

class Cromossomo(object):
    gene = []
    fitness=0


    def __init__(self, cidades,size):
        for i in range(len(cidades)):
            self.gene.append(cidades[i])
        



    def calculafitness(self,matriz):
        for i in range(len(self.gene)-1):
            self.fitness=self.fitness+(matriz[self.gene[i],self.gene[i+1]])
        
    #por troca
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
            




#inicializar cromossomo aleatório



