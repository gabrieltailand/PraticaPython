pessoas = {'nome': 'Maria', 'sexo': 'F', 'idade': 25}
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-' * 30)
pessoas['nome'] = 'Leadro'
pessoas['peso'] = 87.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

