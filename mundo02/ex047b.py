'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

print('Entre 1 e 50, os números pares são:')
for num in range(2, 51, 2):
    if num % 2 == 0:
        print(num, end=" ")
print('ACABOU!')

