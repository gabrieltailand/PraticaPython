'''Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50
por km para viagens de até 200km e R$ 0,45 para viagens mais longas.'''

distancia = float(input('Digite a distancia da sua viagem: '))
if distancia <= 200:
    print('O preço da passagem é de R$ {:.2f} reais'.format(distancia * 0.50))
else:
    print('O preço da passagem é de R$ {:.2f} reais'.format(distancia * 0.45))
print('BOA VIAGEM!')