'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas:
- O nome com todas minúsculas:
- Quantas letras letras ao todo sem considerar espaços:
- Quantas letras tem o primeiro nome.'''

#nome = str(input('Digite aqui seu nome completo: ')).strip()
#print('Analisando seu nome...')
#print('Seu nome em maiúsculas é \033[;35m{}\033[m'.format(nome.upper()))
#print('Seu nome em minúsculas é \033[1;31m{}\033[m'.format(nome.lower()))
#print('Seu nome tem ao todo \033[1;32m{}\033[m letras'.format(len(nome) - nome.count(' ')))
#separa = nome.split()
#print('Seu primeiro nome é \033[1;7;{}\033[m e ele tem \033[1;37m{}\033[m letras'.format(separa[0], len(separa[0])))

nome = str(input('Digite aqui seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é \033[1:31m{}\033[m'.format(nome.upper()))
print('Seu nome em minúsculas é \033[1:32m{}\033[m'.format(nome.lower()))
print('Seu nome tem ao todo \033[1;33m{}\033[m letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()

print('Seu primeiro nome é \033[1:35m{}\033[m e ele possui \033[1:36m{}\033[m letras'.format(separa[0], len(separa[0])))