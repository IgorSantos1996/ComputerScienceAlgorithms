import random
import time

def insertionSort(vetor):
    i = 1  # elemento atual
    while i < len(vetor):
        temp = vetor[i]
        trocou = False
        j = i-1  # elemento anterior ao i, elemento que eu vou comparar
        while j >= 0 and vetor[j] > temp:
            vetor[j+1] = vetor[j]  # empurrando j para frente
            trocou = True
            j = j - 1
        if trocou:
            vetor[j+1] = temp
        i = i + 1


vetor = list(range(0, 10000))
random.shuffle(vetor)
antes = time.time()
insertionSort(vetor)
depois = time.time()
final = (depois - antes) * 1000

print(vetor)

print("O tempo total foi: %0.2f ms " % final)