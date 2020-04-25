'''
Exemplo trivial de utlilizacao
'''
votaram = {}


def verifica_eleitor(nome):
    if votaram.get(nome):  # se ja votou
        print("Mande embora")
    else:
        votaram[nome] = True
        print("Deixe votar!")

verifica_eleitor("tom")
verifica_eleitor("Mike")
verifica_eleitor("Mike")