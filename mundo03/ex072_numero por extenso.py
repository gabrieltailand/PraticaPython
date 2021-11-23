'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

extenso = ('zero', 'Um', 'Dpois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Validação dos números digitados.
while True:
    num = int(input('\033[1;34mDigite um número entre 0 e 20:\033[m '))
    if num >= 0 and num <= 20:
        break
    print('\033[1;31mOpção Inválida. Tente Novamente\033[m')
print(f'\033[1;35mO número digitado foi {extenso[num]}\033[m')


