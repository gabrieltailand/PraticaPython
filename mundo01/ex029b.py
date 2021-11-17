'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.'''

velocidade = float(input('Qual a velocidade? '))
multa = 7 * (velocidade - 80)

if velocidade > 80:
    print('\033[1:31mVocê ultrapassou o limite permitido e será multado!\033[m')
    print('A multa será de R$ \033[1:31m{:.2f}\033[m'.format(multa))
else:
    print('Você está no limite da velocidade permitida.')