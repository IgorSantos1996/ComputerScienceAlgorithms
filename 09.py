'''
Funçao recursiva para calcular se um numero é primo
Caso base: se i for maior que j retorno False
            se o numero  mod i for 0 retorno True
            se nao retorno a funcao passando  o numero, i+ 1 e j
'''


def temdivisor(numero, i, j):
    if i > j:  # divisão com quociente menor que o divisor
        return False
    elif numero % i == 0:  # divisao com resto 0
        return True
    else:
        temdivisor(numero, i+1, j)


def primo(numero):
    return numero > 1 and not (temdivisor(numero, 2, numero-1))


print(primo(223))
