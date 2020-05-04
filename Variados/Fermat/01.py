"""
O ultimo teorema de fermat diz que não há nenhum numero inteiro positivo 
a, b e c tal que a^n + b^n  = c^n, para quaisquer valores de n maiores que 2
Escreva uma função chamada check_format que receba quatro parâmetros , a, b ,c e n
e verifique se o teorema de fermat se mantêm. 
Se n for maior que 2 e a^n + b^n = c^n o programa deve imprimir "Holy smokes, Fermat was wrong!"
Senão o programa deve exibir "No, that doesn't work"

"""

import math


def check_format(a, b, c, n):
    if n > 2 and (math.pow(a, n) + math.pow(b, n) == math.pow(c, n)):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")


check_format(9, 10, 19, 2)
