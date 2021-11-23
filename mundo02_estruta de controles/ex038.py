'''Escreva um programa que leia dois números inteiros compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior:
- O segundo valor é maior:
- Não existe valor maior, os dois são iguais:'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('\033[1;33;7mO primeiro valor é maior.\033[m')
elif n1 < n2:
    print('\033[1;32;7mO segundo valor é maior.\033[m')
elif n1 == n2:
    print('\033[1;36;7mNão existe valor maior, os dois são iguais.\033[m')
print('\033[1;34mBOM TRABALHO!!!\033[m')