'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

nascimento = float(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

print('Você possui {:.0f} anos'.format(idade))

if idade <= 17:
    print('Você ainda irá se alistar ao serviço militar!')
    if idade < 16:
        print('Você irá se alistar em {:.f} anos'.format(18 - idade))
elif idade == 18:
    print('Você já pode se apresentar ao Serviço Militar.')
elif idade > 18:
    print('Você está atrasado {} anos'.format(idade - 18))
    print('ATENÇÃO!!! Você passou do prazo para o alistamento militar, procure a junta da sua cidade.')