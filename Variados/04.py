'''
Busca binária Recursiva na lista
    Caso base: inicio for menor ou igual ao fim
    Caso recursivo:
'''
import time


def busca_bin(listinha, inicio, fim, alvo):
    if inicio <= fim:
        # divisao inteira para pegar o indice do meio da lista
        meio = (inicio+fim) // 2
        if(alvo > listinha[meio]):
            return busca_bin(listinha, meio+1, fim, alvo)
        elif alvo < listinha[meio]:
            return busca_bin(listinha, inicio, meio-1, alvo)
        return meio  # elemento encontrado
    return -1  # elemento não encontrado


lista = list(range(0, 1000000))
elemento = 842

tempo_antes = time.time()
posicao = busca_bin(lista, 0, len(lista)-1, elemento)
tempo_depois = time.time()
total = (tempo_depois - tempo_antes) * 1000  # milisegundos


if(posicao >= 0):
    print("O elemento {} foi encontrado em {}".format(elemento, posicao))
else:
    print("O elemento {} não foi encontrado! ".format(elemento))
print("O tempo gasto foi de %0.2f ms " % total)
