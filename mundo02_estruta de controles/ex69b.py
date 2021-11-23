'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. OBS'''
import datetime
from datetime import date
total18 = 0
totalhomem = 0
totalmulher20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('-' * 25)
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalhomem += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = pergunta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        print('-' * 25)
    if resp == 'N':
        break
print(f'{total18} pessoas tem mais de 18 anos.')
print(f'{totalhomem} homens Cadastrados.')
print(f'{totalmulher20} mulheres com menos de 20 anos.')

