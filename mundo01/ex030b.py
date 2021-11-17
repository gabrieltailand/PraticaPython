'''Crie um progrma que leia um número inteiro e mostre na tela se é  PAR ou ÍMPAR.'''

n = int(input("Digite um número: "))
if n % 2 == 0:
    print('O númerro {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))
