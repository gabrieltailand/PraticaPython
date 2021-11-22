'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final mostre o conteúdo das três listas geradas.'''

valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp not in 'SN':
        print('\033[1;31mOpção inválida!!!\033[m')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-' * 40)
print(f'Você digitou a lista: {valores}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')
