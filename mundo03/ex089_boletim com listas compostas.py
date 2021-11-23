'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

lista = []
while True :
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota1: ')))
    nota2 = (float(input('Nota2: ')))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continujar? [S/N]: ')).strip().upper()
    if resp in "Nn":
        break
print('-' * 35)
print(f'{"No.":<4}{"NOME":<20}{"MÉDIA":>8}')
print('-' * 35)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<20}{a[2]:>8.1f}')
print('-' * 35)

while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if opcao == 999:
        break
        print('FINALIZANDO...')
    if opcao <= len(lista) - 1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')