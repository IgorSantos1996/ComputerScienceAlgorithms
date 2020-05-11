def is_reverse(palavra1='pots', palavra2='stop'):
    if len(palavra1) != len(palavra2):
        return False
    i = 0
    j = len(palavra2)-1

    while j > 0:
        if palavra1[i] != palavra2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print(is_reverse())
