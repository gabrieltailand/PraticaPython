'''Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50
por km para viagens de até 200km e R$ 0,45 para viagens mais longas.'''

distancia = float(input("Qual a distância da viagem em km: "))
t1 = distancia * 0.50
t2 = distancia * 0.45

if distancia <= 200:
    print("O preço da passagem é de R$ {}".format(t1))
else:
    print('O preço da passagem é de R$ {}'.format(t2))
