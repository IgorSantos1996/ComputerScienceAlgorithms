'''
Definição de uma função recursiva para calcular a exponenciação
Caso base: se expoeente = 0, retorno 1
Caso recursivo: retorno  base * fatorial da base, expoente-1  
'''


def exponenciacao(base, expoente):
    assert base != 0
    if expoente == 0:
        return 1
    else:
        return base * exponenciacao(base, expoente-1)


print(exponenciacao(2, 10))
