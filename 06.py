'''Maximo divisor comum recursivo
Caso base:  O caso base é atingido quando algum dos valores é zero. 
Caso recursivo: retorna a chamada da funcao mdc passando o y e o resto de x mod y
'''

def mdc(x, y):
    if x == 0 or y == 0:
        return x+y
    else:
        return mdc(y, x % y)
