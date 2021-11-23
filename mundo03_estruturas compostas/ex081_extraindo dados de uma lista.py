'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp not in 'SN':
        print('\033[1;31mOpção inválida!\033[m')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-' * 30)
print(f'Você digitou a lista: {valores}')
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')