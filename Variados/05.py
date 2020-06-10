'''
funcao para calcular o fatorial de um numero, recursivamente

Caso base: se o numero for 0, retorno 1
Caso Recursivo: retorno o numero  multiplicado pelo fatorial dele -1
'''
import pytest
import time


def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x-1)


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6)
])

def testa_fatorial (entrada, esperado):
    assert fatorial(entrada) == esperado

#tempo_antes = time.time()
#print(fatorial(900))
#tempo_depois = time.time()
#print("O tempo decorrido: {} segundos".format
#(tempo_depois-tempo_antes) * 1000))
