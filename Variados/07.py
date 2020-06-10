'''
Implementar uma função media que calcule o valor médio de uma lista de números
 
'''

def somarecursiva(minha_lista):
    if len(minha_lista) == 0:
        return 0
    else:
        return minha_lista[0] + somarecursiva(minha_lista[1:])


def media(lista):
    if lista == []:
        print("erro, lista vazia")
    else:
        return somarecursiva(lista)/len(lista)


print((media([2, 2, 6])))
