def fib(n):
    lista_fibonnaci = []
    a, b = 0, 1
    while b < n:
        # lista_fibonnaci.append(b)
        lista_fibonnaci = lista_fibonnaci + [b]
        a, b = b, a + b
    return lista_fibonnaci


print(fib(100))
