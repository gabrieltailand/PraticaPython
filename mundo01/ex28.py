'''Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador'''

import random
from time import sleep
n = int(input('What is your guess?: '))

list = [0, 1, 2, 3, 4, 5]
choosen = random.choice(list)
print('The number is {}'.format(choosen))

print('LOADING...')
sleep(3)

if n == choosen:
    print('\033[1;7;44mYou win! CONGRATULATIONS!\033[m')
else:
    print('\033[1;7;41mYou have failed, try again!\033[m')












