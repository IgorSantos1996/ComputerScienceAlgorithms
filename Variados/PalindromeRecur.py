def ispalindromo(s: str):
    if len(s) <= 1: #uma letra ou nenhuma
        return True
    if s[0] != s[-1]: # se a primeira letra já for diferente da ultima, ja era.
        return False
    return ispalindromo(s[1:-1]) # se chegar aqui, ele vai comparando letra a letra, começando da segunda e da penultima,
 
"""
chamada para arara
1 - a, 2 - r, 3 - a, 4 - a, 5 - a
Compara 2 com 4
"""
print("allen"[1:-1])

print(ispalindromo('allen'))
print(ispalindromo('bob'))
print(ispalindromo('otto'))
print(ispalindromo('redivider'))
