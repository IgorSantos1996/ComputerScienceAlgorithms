'''Maximo divisor comum recursivo
Caso base:  O caso base é atingido quando algum dos valores é zero. 
'''


def mdc(x, y):
    if x == 0 or y == 0:
        return x+y
    else:
        return mdc(y, x % y)
