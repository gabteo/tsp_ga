import cromossomo
import random

class crossover(object):
    def __init__(self, pai1, pai2, method):
        if (method == "pmx") or (method == "PMX"):
            self.pmx(pai1, pai2)
        elif (method == "ox") or (method == "OX"):
            self.ox(pai1, pai2)
        elif (method == "cx") or (method == "CX"):
            self.cx(pai1, pai2)

    def pmx(self, pai1, pai2):
        return

    def ox(self, pai1, pai2):
        if len(pai1) == len(pai2):
            cutA = random.randint(0, len(pai1))
            cutB = random.randint(0, len(pai1))

        filho1 = cromossomo(len(pai1))
        filho2 = cromossomo(len(pai1))

        filho1[cutA:cutB] = pai1[cutA:cutB]
        filho2[cutA:cutB] = pai2[cutA:cutB]

        #copiar pais para poder deletar elementos~
        pai1_copia = []
        pai2_copia = []

        for i in range(len(pai1)):
            pai1_copia[i] = pai1[1]
            pai2_copia[i] = pai2[1]

        cutLen = cutB - cutA
        for i in range(cutLen):
            #pai1_copia.remove()


        return [pai1, pai2]

    def cx(self, pai1, pai2):
        return