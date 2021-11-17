"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. """

n = int(input("Digite o número: "))
print('''Escolha uma das bases para comnversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[0;31mOção inválida. Tente novamente!\033[m')

