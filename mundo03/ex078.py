'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.'''

valores =list()
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'A lista digitada foi: {valores}')
print(f'{maior} foi o maior número digitado e ele está nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'{menor} foi o menor número digitado e ele está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()







