def cumsum(listinha):
    soma = 0
    novalista = []
    
    for x in listinha:
        soma += x
        novalista.append(soma)
    return novalista

print(cumsum([1 , 2 , 3]))
print(list(range(1, 10)))