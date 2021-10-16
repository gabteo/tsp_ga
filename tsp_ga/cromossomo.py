from collections import Sequence
import cidades

class Cromossomo(object):
    #gene = []
    #fitness = 0

    def __init__(self, Cidades, size):
        self.gene = []
        self.fitness = 0

        #print(type(Cidades))
        #print(Cidades)
        #l=len(Cidades)
        #print(l)
        #l = int(Cidades)-1
        for i in range(len(Cidades)):
            self.gene.append(Cidades[i])
        #self.fitness()

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

    def fitness(self):
        for i in range(len(self.gene)):
            #self.fitness += cidades.dist(self.gene[i], self.gene[i-1])
            pass

    def getFitness(self):
        return self.fitness
            




#inicializar cromossomo aleatório



