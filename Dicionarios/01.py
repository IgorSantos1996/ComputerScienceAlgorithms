def histogram(s):
    d = dict()
    for c in s:  # para cada caracter na string s
        # se o caractere (como chave) não estiver no dicionario
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d


# print(histogram('abracadabra'))

def histogram_sem_if(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 1)
    return d


print(histogram_sem_if('abracadabra'))
