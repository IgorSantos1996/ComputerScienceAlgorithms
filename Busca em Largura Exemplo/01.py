from collections import deque


grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    print("Estado da fila: ", fila_de_pesquisa)
    verificadas = []  # os que ja foram verificados
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:  # verifica a pessoa somente se ela já não tiver sido verificadas
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga! ")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)  # marca a pessoa como verificada


pesquisa("voce")
