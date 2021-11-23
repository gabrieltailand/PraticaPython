"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo."""

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('digite o comprimento da terceira reta: '))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r3 + r2

if soma1 > r3 and soma2 > r2 and soma3 > r1:
    print('\033[1;35mAs três retas PODEM FORMAR um triângulo\033[m')
else:
    print('\033[1;31mNÃO É POSSÍVEL formar um triângulo com as retas a cima.\033[m')
