'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

import math
totcompra = 0
somapreco = 0
baratoproduto = 0
baratopreco = 0
caropreco = 0
quantpreco = 0
maior = 0
menor = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: R$ '))
    print('-' * 20)
    totcompra += preco

    if preco > 1000:
        somapreco += 1
    if quantpreco == 1:
        maior = menor = preco
    else:
        if preco > maior:
            maior = preco
            if preco < menor:
                menor = preco
    if preco == menor:
        baratoproduto = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('-' * 20)
    if resp == 'N':
        break
print(f'\033[1;32mO total da compra foi de R$ {totcompra:.2f}.\033[m')
print(f'\033[1;33m{somapreco} produtos custam mais que R$ 1000 reais.\033[m')
print(f'\033[1;34mO produto mais barato foi {produto}\033[m')
