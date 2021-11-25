'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('CTPS [0 PARA FINALIZAR]: '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Slário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}.')


