'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor = 0

for pess in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.2f}kg'.format(maior))
print('O menor peso é {:.2f}kg'.format(menor))

