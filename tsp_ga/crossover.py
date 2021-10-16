import cromossomo
import random

class crossover(object):
    # lembrar de conferir se funciona com classe cromossomo
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

        if len(pai1) is not len(pai2):
            print("Erro: os pais tem tamanho diferente")
            return

        # sorteio da posição dos cortes A e B
        cutA = random.randint(0, len(pai1))
        cutB = random.randint(0, len(pai1))

        # sorteia outro corte, caso os originais sejam iguais
        while cutA == cutB:
            cutB = random.randint(0, len(pai1))

        # ordena cortes, para que cutA < cut B
        if cutB > cutA:
            aux = cutA
            cutA = cutB
            cutB = aux

        # inicializando cromossomos filhos com o mesmo tamanho dos pais
        filho1 = cromossomo(len(pai1))
        filho2 = cromossomo(len(pai1))

        # copiando para os filhos a parte dos cromossomos pais entre os cortes
        filho1[cutA:cutB] = pai1[cutA:cutB]
        filho2[cutA:cutB] = pai2[cutA:cutB]

        # copiar pais sem elementos que já estão nos filhos
        # inicializando cromossomos vazios para a cópia:
        pai1_copia = cromossomo(len(pai1))
        pai2_copia = cromossomo(len(pai1))

        '''
        for i in range(len(pai1)):
            pai1_copia[i] = pai1[1]
            pai2_copia[i] = pai2[1]
        for i in range(cutA, cutB):
            pai1_copia.remove(pai1[i])
            pai2_copia.remove(pai2[i])
        '''

        # começando pelo corte B, copia pai1 para pai1_copia, 
        # sem os elementos que já estão em filho 2
        for i in range(cutB, len(pai1)):
            if pai1[i] not in filho2:
                pai1_copia.append(pai1[i])
        for i in range(cutB):
            if pai1[i] not in filho2:
                pai1_copia.append(pai1[i])

        # o mesmo para o pai 2 e filho 1
        for i in range(cutB, len(pai2)):
            if pai2[i] not in filho1:
                pai2_copia.append(pai2[i])
        for i in range(cutB):
            if pai2[i] not in filho1:
                pai2_copia.append(pai2[i])


        # agora, adiciona-se aos filhos os elementos copiados,
        # iniciando pelo primeiro elemento dos pais copiados, que 
        # serão adicionados aos filhos a partir do corte B deles
        j = cutB
        for i in range(len(pai1_copia)):    # i é index do pai
            if j == len(filho2):            # j é index do filho
                #volta pro começo do filho se já tiver feito o final
                j = 0
            elif (j < len(filho2)) and (j >= cutB): 
                # final do filho         
                filho2[j] = pai1_copia[i]
                j += 1
            elif (j < len(filho2)) and (j < cutA):
                # primeira parte do filho
                filho2[j] = pai1_copia[i]
                j += 1
            elif j == cutA:
                break


        return [filho1, filho2]

    def cx(self, pai1, pai2):
        return