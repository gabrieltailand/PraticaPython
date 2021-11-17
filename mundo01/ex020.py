'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um
programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
n1 = str(input('\033[1;34mPrimeiro aluno: '))
n2 = str(input('\033[1;33mSegundo aluno: '))
n3 = str(input('\033[1;37mTerceiro aluno: '))
n4 = str(input('\033[1;35mQuarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)