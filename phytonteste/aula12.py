nome = str(input('Quel é o seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome femenino')
else:
    print('Seu nome é bem normal')
print('\033[1;33mTenha um bom dia, {}!\033[m'.format(nome))
