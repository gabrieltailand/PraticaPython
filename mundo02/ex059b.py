'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
import math
from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('-' * 30)
print('Opções:')
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
print('-' * 30)
opção = int(input('Escola uma opção: '))
while opção != 5:
    if opção == 1:
        soma = valor1 + valor2
        print('A soma entre os dois valores é {}'.format(soma))
        opção = int(input('Escolha uma opção: '))
    if opção == 2:
        multiplicação = valor1 * valor2
        print('O produto dos dois valores é {}'.format(multiplicação))
        opção = int(input('Escolha uma opção: '))
    if opção == 3:
        maior = max(valor1, valor2)
        print('O maior valor é {}'.format(maior))
        opção = int(input('Escolha uma opção: '))
    if opção == 4:
        print('\033[1;32mINSIRA NOVOS VALORES!!!\033[m')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        opção = int(input('Escolha uma opção: '))
    if opção == 5:
        print('Finalizando...')
    else:
        print('Escolha inválida. Tente novamente.')
        opção = int(input('Escolha uma opção válida: '))
print('\033[1;35mFinalizando...\033[m')
sleep(2)
print('=-=' * 10)
print('\033[1;34mFim do programa. Volte sempre!\033[m')



