import bisect

"""Implementando manualmente"""


def in_bisect(listinha, valor_alvo):
    if len(listinha) == 0:
        return False

    meio = len(listinha) // 2
    if(listinha[meio] == valor_alvo):
        return True
    if valor_alvo < listinha[meio]:
        return in_bisect(listinha[:meio], valor_alvo)
    else:
        return in_bisect(listinha[meio+1:], valor_alvo)


"""Com a ajuda do modeulo bisect"""


def in_bisect_library(listinha, valor_alvo):
    i = bisect.bisect_left(listinha, valor_alvo)
    if i == len(listinha):
        return False
    return listinha[i] == valor_alvo


#in_bisect([1, 2, 3, 4, 5, 5], 2)
for word in ['aa ', 'alien', 'allen', 'zymurgy']:
    print(word, ' in list ', in_bisect(['h', 'b', 'r', 'a', 'c', 'f'], 'c'))


def busca_bin_seq_itera(listinha, alvo):
    primeiro = 0
    ultimo = len(listinha)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if listinha[meio] == alvo:
            return meio
        else:
            if alvo < listinha[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return -1