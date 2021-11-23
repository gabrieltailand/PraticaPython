'''Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo
o nome deles e escrevendo o nome escolhido.'''

import random

a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o seguno aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print('O Aluno escolhido foi {}'.format(escolhido))
