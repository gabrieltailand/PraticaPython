'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequência de Fibonacci.

Ex:
0, 1, 1, 2, 3, 5, 8'''

print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
n = int(input('Quantos números você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 20)
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
print('~' * 20)