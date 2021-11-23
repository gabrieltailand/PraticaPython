'''Faça um programa que faça a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''



while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        tabuada = n * c
        print(f'{n} x {c:2} = {tabuada:2}')
    print('-' * 30)
print('Programa de Tabuada encerrado, volte sempre!')