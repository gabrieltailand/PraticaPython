'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Você têm {}'.format(idade))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamente!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Ainda faltan {} anos para o alistamento militar'.format(18 - idade))
