'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Digite um número: '))
print('-' * 12)
for c in range(1, 11):
    tabuada = n * c
    print('{} x {:2} = {:2}'.format(n, c, tabuada))
print('-' * 12)
print('FIM')
