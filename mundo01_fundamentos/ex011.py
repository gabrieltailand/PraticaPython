largura = float(input('Digite a Largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
tinta = area / 2
print('\033[1;7mSua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²\033[m'.format(largura, altura, area))

print('\033[1;44;7mPara pintar essa parede, você precisará de {:.2f}L de tinta\033[m'.format(tinta))


