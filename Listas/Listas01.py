def nested_sum(listinha: list):
    print(list)
    soma = 0
    for x in listinha:
        for i in x:
            soma += i
    print(soma)


nested_sum([[1, 2], [3], [4, 5, 6]])
