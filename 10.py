''' 
funcao para calcular a sequencia de fibonacci
Caso base: if numero for igual a 0 ou 1, retorno 1
Caso recursivo: retorno fibonacci de n-1, fibonacci de n-2

Obs: Solução extramamente ineficiente
A razão para esta ineficiência é simples: por exemplo, para calcular fibonacci(35) é necessário calcular fibonacci(34) 
e fibonacci(33), mas o cálculo de fibonacci(34) também necessita de calcular fibonacci(33),
que é portanto calculado 2 vezes; é fácil perceber que então fibonacci(32) será calculado 3 vezes, 
fibonacci(31) será calculado 5 vezes e assim sucessivamente, dando origem a um processo (pior do que) exponencial.
'''


def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print([fibonacci(i) for i in range(8)])
