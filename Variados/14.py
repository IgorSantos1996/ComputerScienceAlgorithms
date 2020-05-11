
def  count (palavra='banana'):
    contador = 0
    for letter in palavra:
        if letter == 'a':
            contador = contador + 1
    print(contador)