"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor, da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. """

valor = float(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite seu salário: R$ '))
periodo = int(input('Em quantos anos deseja pagar? '))

mensalidade = valor / (periodo * 12)
margem = (salario * (30 / 100))

print('-' * 60)
print('O valor do imóvel é R$ {:.2f} Reais'.format(valor))
print('Seu salário é R$ {:.2f} Reais'.format(salario))
print('O período de financiamento será em {} anos'.format(periodo))
print('A prestação é de R$ {:.2f} Reais'.format(mensalidade))
print('Seu limite mensal para financiamento é de R$ {} Reais'.format(margem))
print('-' * 60)

if mensalidade >= margem:
    print('Você execeu 30% da margem permitida, Seu empréstimo será \033[1;31mNEGADO!\033[m')
else:
    print("Seu empréstimo foi \033[1;34mAPROVADO\033[m")

