def funcao():
    global n1 # usa a variável global
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2 # usando o global dentro da função, esta variável perde o valor.
funcao()
print(f'N1 fora vale {n1}')