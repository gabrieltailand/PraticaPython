'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade.

- Até 9 ano MIRIM;
- Até 14 anos INFANTIL;
- Até 19 anos JUNIOR;
- Até 20 anos SENIOR;
- Acima MASTER'''

from datetime import date
ano = int(input('Digite aqui o ano de nascimento: '))
idade = date.today().year - ano


if idade <= 9:
    print('Você possui {} anos. Sua categoria é \033[1;32mMIRIM.\033[m'.format(idade))
elif idade > 9 and idade <=14:
    print('Você possui {} anos. Sua categoria é \033[1;33mINFANTIL.\033[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você possui {} anos. Sua categoria é \033[1;34mJUNIOR.\033[m'.format(idade))
elif idade == 20:
    print('Você possui {} anos. Sua categoria é \033[1;35mSENIOR.\033[m'.format(idade))
elif idade > 20:
    print('Você possui {} anos. Sua categoria é \033[1;36mMASTER.\033[m'.format(idade))

