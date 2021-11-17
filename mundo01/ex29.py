'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.'''

vel = float(input('Qual a velocidade do carro?: '))
limite = 80
multa = 7 * (vel - limite)

if vel >= limite:
    print('\033[31mVocê excedeu o limite de velocidade. Você será multado!\033[m')
    print('\033[34mO valor da multa é de R$ {:.2f}\033[m'.format(multa))
print('\033[1;7;40mTenha um bom dia. Dirija com segurança!\033[m')
