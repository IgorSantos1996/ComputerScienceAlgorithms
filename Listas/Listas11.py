def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def encontra_pares_inversos(listinha):
    lisaux = []
    for item in range(len(listinha)-1):
        if not is_palindrome(listinha[item]):
            listinha.pop(item)
        if listinha.count(listinha[item]) > 1:
            indice = item
            lisaux.append(listinha[indice])
    return lisaux


lista = ['arara', 'aba', 'bob', 'arara', 'osso', 'cara', 'osso']

print(encontra_pares_inversos(lista))
