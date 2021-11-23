'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random
# Sorteio de valor
num_gerados = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
               random.randint(1, 10))
print(f'O números sorteados forma: {num_gerados}')
# Maior e menor valor
print(f'O maior valor sorteado foi: {max(num_gerados)}')
print(f'O menor valor sorteado foi: {min(num_gerados)}')
