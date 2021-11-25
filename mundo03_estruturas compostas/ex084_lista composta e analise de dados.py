'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
contpess = 0
somapess = 0
pesados = 0
leves = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso em Kg: ')))
    # Calculando o mais pesado e o mais leve.
    if len(pessoas) == 0:
        pesados = leves = dados[1]
    else:
        if dados[1] > pesados:
            pesados = dados[1]
        if dados[1] < leves:
            leves = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]

    if resp not in 'SN':
        print('\033[1;31mOpção Inválida! Tente novamente.\033[m')
        resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]

    if resp in 'N':
        break
print('-' * 40)
# Calculando a soma de pessoas cadastradas.
for p in pessoas:
    contpess += 1
    somapess += 1
print(f'A soma das pessoas cadastradas foi {somapess}.')
# Apurando o maior peso.
print(f'O maior peso foi {pesados}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesados:
        print(f'[{p[0]}] ', end='')
print()
# Apurando o menor peso.
print(f'O menor peso foi {leves}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leves:
        print(f'[{p[0]}] ', end='')
print()

