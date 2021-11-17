nome = input('Digite um produto: ')
preço = float(input('Digite o valor do produto: '))
vista = preço - (preço * 0.05)
parcelado = preço + (preço * 0.025)

print('Um {} que custa R${:.2f}, se comprado à vista, o seu valor é de R${:.2f}'.format(nome, preço, vista))
print('Se comprado parcelado, o valor é R${:.2f}'.format(parcelado))

