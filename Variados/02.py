'''
Função recursiva que conte o numero de itens em uma lista
Caso base: Se a lista estiver vazia retorno 0
Caso recursivo: retornar 1 + chamada da funcao passando todos os demais elementos da lista, ou seja, [1:]
'''


def somarqtditens(minha_lista):
    if minha_lista == []:
        return 0
    else:
        return 1 + somarqtditens(minha_lista[1:])


print(somarqtditens([1, 5, 1, 8, 47, 8, 5]))
