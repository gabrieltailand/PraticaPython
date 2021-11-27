'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep


def sorteio(lista): # Função sorteio
    print('Sorteio de 5 valores... ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('FIM!')


def somapar(lista): # Função SomaPar
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores PARES de {lista}, temos: {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)

