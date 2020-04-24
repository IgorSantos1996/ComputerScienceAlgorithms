import random


def Bubblesort(lista):
    fim = len(lista)
    while fim > 0:
        i = 0
        # Percorrendo a lista de 0 até o fim
        while i < fim - 1:
            if lista[i] > lista[i+1]:
                # Realizando a troca  da posicao atual pela proxima
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
            i = i + 1
        fim = fim - 1


vetor = list(range(0, 10000000))
random.shuffle(vetor)
print("Vetor desordenado", vetor)
Bubblesort(vetor)
print("vetor ordenado ", vetor)
