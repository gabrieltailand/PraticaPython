"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua 
categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date
nascimento = float(input('Digite o ano de nascimento do atleta: '))
print('*' * 30)
print('''- Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER''')
print('*' * 30)
atual = date.today().year
idade = atual - nascimento

print('O atleta que nasceu em {:.0f} tem {:.0f} anos'.format(nascimento, idade))

if idade < 9:
    print('Sua categoria é MIRIM.')
elif idade >= 9 and idade < 14:
    print('Sua categoria é INFANTIL.')
elif idade >= 14 and idade < 19:
    print('Sua categoria é JÚNIOR.')
elif idade >= 19 and idade < 25:
    print('Sua categoria é SÊNIOR.')
elif idade >= 25:
    print('Sua categoria é MASTER')