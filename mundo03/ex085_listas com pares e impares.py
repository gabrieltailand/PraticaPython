'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite um {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-' * 40)
numeros.sort()
print(f'A lista digitada foi: {numeros}')
numeros[0].sort()
print(f'A lista de números PARES é: {numeros[0]}')
numeros[1].sort()
print(f'A lista de números ÍMPARES é: {numeros[1]}')