import random
import time


def Selectionsort(lista):
    i = 0
    while i < len(lista) - 1:  # o i percorre somente até a penultima posicao
        menor = i  # o primeiro elemento é sempre o menor
        j = i + 1  # estara sempre uma posicao à frente do i
        # em busca do menor elemento
        while j < len(lista):
            if lista[j] < lista[menor]:
                menor = j
            j = j + 1
        # verifica se precisa realizar a troca
        if menor != i:
            temp = lista[i]
            lista[i] = lista[menor]
            lista[menor] = temp
        i = i + 1


lista = list(range(0, 10000))
random.shuffle(lista)
antes = time.time()
Selectionsort(lista)
depois = time.time()
total = (depois - antes) * 1000

print(lista)
print("O tempo total para ordenar foi de: %0.2f ms" % total)
