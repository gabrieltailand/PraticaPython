np = float(input('Digite a nota de Português: '))
nm = float(input('Digite a nota de Matemática: '))
s = np + nm
m = s / 2
print('A média do aluno é {:.2f}'.format(m))
if m < 5:
    print('\033[31mVocê não tirou a média necessária. Estude Mais\033[m')
else:
    print('\033[1;34mParabéns, você passou!\033[m')



