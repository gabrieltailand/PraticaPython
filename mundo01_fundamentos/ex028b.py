import random
from time import sleep
n = int(input('Qual é o seu palpite?: '))

lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)

print('\033[1:34mLOADING...\033[m')
sleep(3)
print('O número é {}'.format(escolhido))

if n == escolhido:
    print('\033[1:33mVocê venceu, Parabéns!!!\033[m')
else:
    print('\033[1:31mVocê perdeu, tente novamente!\033[m')
