'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoas = dict()
lista = list()
cont = 0
somaidade = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    # Validação do sexo.
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    somaidade += pessoas['idade']
    lista.append(pessoas.copy())
    # Validação de resposta.
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')

    if resp in 'N':
        break
print('-' * 30)
# A) Quantas pessoas foram cadastradas
for c in lista:
    cont += 1
print(f' - Ao todo foram cadastradas {cont} pessoas.')
# B) A média de idade
media = somaidade / len(lista)
print(f' - A média de idade é de {media:5.2f} anos.')
# C) Uma lista com as mulheres
print(' - As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
# D) Uma lista de pessoas com idade acima da média
print(' - Lista das pessoas que possuem idades acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('--- FIM DO PROGRAMA ---')



