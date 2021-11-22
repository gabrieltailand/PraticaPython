'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

valores = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        valores.append(n)
    elif n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(f'A lista digitada foi: {valores}')
