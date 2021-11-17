'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
v1 = int(input('\033[32mPrimeiro valor:\033[m '))
v2 = int(input('\033[33mSegundo valor:\033[m '))
escolha = 0
while escolha != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    escolha = int(input('\033[36m>>>> Qual a sua escolha? \033[m'))
    if escolha == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1, v2, soma))
    elif escolha == 2:
        produto = v1 * v2
        print('O resultado de {} e {} é {}'.format(v1, v2, produto))
    elif escolha == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior número é {}'.format(v1, v2, maior))
    elif escolha == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Escolha inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')
