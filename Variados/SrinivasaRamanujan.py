import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def estimate_pi():
    pi = 0
    k = 0
    fator = 2 * math.sqrt(2) / 9801
    while True:
        numerador = factorial(4 * k) * (1103 + 26390*k)
        denominador = factorial(k)**4 * 396 ** (4*k)
        termo = fator * numerador / denominador
        pi = pi + termo

        if termo < 1e-15: # mesmo que 10 elevado a 15
            break
        k = k + 1
    return 1 / pi


print(estimate_pi())
