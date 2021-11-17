'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''


while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        tabuada = num * c
        print(f'{num} x {c:2} = {tabuada:2}')
    print('-' * 30)
print('Programa de tabuada acerrado. Volte sempre!')



