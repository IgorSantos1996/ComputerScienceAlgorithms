
def rotate_letter(s: str, numero):
    """
    Retorna uma nova string que contém as letras da string original rotacionadas pelo numero dado
    """
    posicao = ord(s) - ord('a')
    i = (posicao + numero) % 26 + ord('a')
    return chr(i)


def rotate_word(s: str, numero):
    res = ''
    for item in s:
        res += rotate_letter(item, numero)
    return res


print(rotate_word('cheer', 7))
