'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida.'''

peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é \033[1;33m{:.2f}\033[m. Você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é \033[1;34m{:.2f}\033[m. Você está no peso seu ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é \033[1;35m{:.2f}\033[m. Você está com sobrepeso'.format(imc))
elif imc >30 and imc <= 40:
    print('Seu IMC é \033[1;36m{:.2f}\033[m. Você está Obeso'.format(imc))
elif imc >40:
    print('Seu IMC é \033[1;31m{:.2f}\033[m. Você está com Obesidade Mórbida'.format(imc))