'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor,
da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

vcasa = float(input('Qual o valor do imóvel? '))
vsalario = float(input('Qual o seu salário? '))
periodo = int(input('Em quantos anos você quer pagar? '))
prestacao = vcasa / (periodo * 12)
limite = vsalario * 0.30

print('-' * 60)
print('O valor da casa é \033[0;32mR$ {:.2f} Reais\033[m'.format(vcasa))
print('Seu salário é: \033[0;33mR$ {:.2f} Reais\033[m'.format(vsalario))
print('O período do financiamento será em \033[0;34m{} anos\033[m'.format(periodo))
print('A prestação é de \033[0;35mR$ {:.2f} Reais\033[m'.format(prestacao))
print('Seu limite mensal para financiamento é de \033[0;35mR$ {:.2f} Reais\033[m'.format(limite))
print('-' * 60)

if prestacao > limite:
    print('\033[1;31mVocê excedeu 30% do seu salário. Seu empréstimo foi NEGADO.\033[m')
else:
    print('\033[1;34mSeu empréstimo foi APROVADO.\033[m')
