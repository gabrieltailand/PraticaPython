"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

preco = float(input('Digite o valor do produto: R$ '))
print('-' * 30)
print('''FORMA DE PAGAMENTO
[ 1 ] Cash
[ 2 ] Card
[ 3 ] Parcelado 1
[ 4 ] Parcelado 2''')
print('-' * 30)
opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
   cash = preco - (preco * 0.1)
   print('Escolhendo a opção 1, o valor a ser pago é de R${:.2f}'.format(cash))
elif opcao == 2:
    card = preco - (preco * 0.05)
    print('Escolhendo a opção 2, o valor a ser pago é de R${:.2f}'.format(card))
elif opcao == 3:
    parc1 = preco
    parcela = parc1 / 2
    print('Escolhendo a opção 3, o valor a ser pago é de R${:.2f}'.format(parc1))
elif opcao == 4:
    parc2 = preco + (preco * 0.2)
    print('Escolhendo a opção 4, o valor a ser pago é de R${:.2f}'.format(parc2))
