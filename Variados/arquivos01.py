fin = open(
    'C:\\Users\\Igor\\Desktop\\algorithms\\ComputerScienceAlgorithms\\Variados\\words.txt')
for line in fin:
    if len(line.strip()) > 19 and 'e' not in line:
        print(line)


def has_no_e(word: str):
    if 'e' not in word:
        return True
    return False


def avoids(word, forbidden1, forbidden2, forbidden3):
    cont = 0
    if forbidden1 and forbidden2 and forbidden3 not in word:
        cont = cont + 1
        return True
    return False


def uses_only(word, availlable):
    for letter in word:
        if letter not in availlable:
            return False
    return True


def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


def uses_all(word, required):
    return uses_only(required, word)


def is_abecedarian(word):
    primeira = word[0]
    for c in word:
        if c < primeira:
            return False
        primeira = c
    return True


def is_abecedarian_recu(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    is_abecedarian_recu(word[1:])
