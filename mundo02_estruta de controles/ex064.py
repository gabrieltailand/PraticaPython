'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
 o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
 desconsiderando o flag.'''

cont = 0
soma = 0
n = int(input('Digite um valor: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(cont, soma))
