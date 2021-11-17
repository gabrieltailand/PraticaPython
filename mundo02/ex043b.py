'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print('Seu IMC é de \033[1;33m{:.1f}\033[m. Você está no peso ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMc é de \033[1;34m{:.1f}\033[m. Você está no peso IDEAL'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é de \033[1;34m{:.1f}\033[m. Você está com SOBREPESO.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de \033[1;34m{:.1f}\033[m. Você está OBESO.'.format(imc))
elif imc > 40:
    print('Seu IMc é de \033[1;31m{:.2f}\033[m. Você está com OBESIDADE MÓRBIDA'.format(imc))