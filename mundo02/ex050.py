'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
