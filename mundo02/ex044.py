'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento.

- À vista no dinheiro: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros.'''

print('{:=^40}'.format(' LOJAS GABRIELA '))

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} de R$ {:.2f} COM JUROS!'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO DE PAGAMENTO INVÁLIDA. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))



