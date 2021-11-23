'''Crie um programa que mostre na tela  todos os números pares que estão  no intervalo de 1 a 50'''


for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('ACABOU')