"""
Escreva uma função chamada is_triangle que receba três números inteiros como argumentos, e que imprima “Yes” ou “No”, 
dependendo da possibilidade de formar ou não um triângulo de gravetos com os comprimentos dados.
"""


def is_triangulo(a, b, c):
    if a > b + c:
        print("No")
        return False
    elif b > a + c:
        print("No")
        return False
    elif c > a + b:
        print("No")
        return False
    else:
        print("Yes")
        return True

is_triangulo(1,2,3)