'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('\033[32mValor adicionado com sucesso.\033[m')
    else:
        print('\033[33mValor duplicado. Não será possível adicioná-lo.\033[m')
    resp = ''
    resp = str(input('Quer continuar [S/N] ? ')).strip().upper()
    if resp == 'N':
        break
print('-' * 40)
valores.sort()
print(f'\033[32mA lista digitada foi: {valores}\033[m')