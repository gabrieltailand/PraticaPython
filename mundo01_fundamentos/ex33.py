'''Faça um programa que mostre três números e mostre qual é o maior e qual é o menor.'''

import math
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = [n1, n2, n3]

print('O número maior é {}'.format((max(lista))))
print('O número menor é {}'.format(min(lista)))
