def consec (word):
    i = 0
    contador = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            contador = contador + 1
            if contador == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2 * contador
            contador = 0
    return False
 
consec('aabsbcc')