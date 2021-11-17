'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$1.250,00, calcule um aumeto de 10%.
- Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual o valor do salário?: '))
aumento1 = salario + (salario * 0.10)
aumento2 = salario + (salario * 0.15)

if salario > 1250:
    print('Seu novo salário é de R$ {:.2f}'.format(aumento1))
else:
    print('Seu novo salário é de R$ {:.2f}'.format(aumento2))
