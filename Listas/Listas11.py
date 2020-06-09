
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def encontra_pares_inversos(listinha):
    for item in range(len(listinha)-1):
        if is_palindrome(listinha[item]):
            print(item)


lista = ['osso', 'aba', 'bob', 'arara', 'arara', 'cara', 'osso']


encontra_pares_inversos(lista)
