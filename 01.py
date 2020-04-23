'''
Soma recursiva de elementos de uma lista

Caso base: Se a lista estiver vazia retorno 0
Caso Recursivo: retorno o primeiro elemento da lista somando com todos os demais elementos dela.
'''


def somarecursiva(minha_lista):
    if len(minha_lista) == 0:
        return 0
    else:
        return minha_lista[0] + somarecursiva(minha_lista[1:])


print(somarecursiva([2, 2]))
