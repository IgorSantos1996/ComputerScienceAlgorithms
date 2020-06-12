class Ordenador:
    def selecao_direta(self, lista):
        for i in range(len(lista) - 1):
            posicao_do_minimo = i
            for j in range(i + 1, len(lista)-1):  # depois da posicao i até o fim
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            # Coloca o menor elemento encontrado no inicio da sublista
            # Para isso, troca de lugar os elementos nas posicoes i e posicao do minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


lista = [10, 3, 8, -10, 200, 17, 32]

