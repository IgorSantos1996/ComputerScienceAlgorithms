'''
Função recursiva para encontrar o valor mais alto em uma lista
Caso base: se a lista não tiver nenhum elemento.
Caso recursivo: chama funcao verifica passando o primeiro elemento da lista e os demais valores da lista
'''


def valor_mais_alto(minha_lista):
    if minha_lista == []:
        return 0
    else:
        return verifica(minha_lista[0], valor_mais_alto(minha_lista[1:]))


def verifica(x, y):
    if x > y:
        return x
    else:
        return y


print(valor_mais_alto([7, 8, 200, 1, -1, 300]))
