from time import time


"""Lê as linhas do arquivo e constroi uma lista usando a funcao append()"""
def make_list():
    t = []
    arquivo = open(
        'C:\\Users\\Igor\\Desktop\\algorithms\\ComputerScienceAlgorithms\\Variados\\Listas\\words.txt', 'r')
    for line in arquivo:
        conteudo = line.strip()
        t.append(conteudo)
    return t

"""Lê as linhas do arquivo e constroi uma lista usando somente o operador +."""
def make_list2():
    t = []
    arquivo = open(
        'C:\\Users\\Igor\\Desktop\\algorithms\\ComputerScienceAlgorithms\\Variados\\Listas\\words.txt', 'r')
    for line in arquivo:
        conteudo = line.strip()
        t = t + [conteudo]
    return t


''' Comparecao de tempo entre as duas funcoes acima'''
comecou = time()
first = make_list()
elapsed_time = time() - comecou

print(first)
print(elapsed_time, 'seconds')

comecou = time()
second = make_list2()
elapsed_time = time() - comecou

print(len(second))
print(elapsed_time, 'seconds')

