'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('TV', 1200, 'Geladeira', 800, 'Sofá', 2000, 'Fogão', 400, 'Arcondicionado', 700, 'Cama', 1100, 'Panela',
            75, 'Lençol', 45, 'Filtro', 300, 'Guarda-Roupa', 650)
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
print('-' * 40)