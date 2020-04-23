'''
Algoritmo de ordenação quicksort
'''

import random


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        # escolhe como pivo o primeiro elemento da extema esquerda
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quickSort(menores) + [pivo] + quickSort(maiores)
        # chama o quicksort para o sub-array dos menores e para o sub-array dos maiores


myarray = list(range(0, 1000))  # cria uma lista com valores entre os limites

random.shuffle(myarray)  # embaralha os elementos da lista
print(quickSort(myarray))
