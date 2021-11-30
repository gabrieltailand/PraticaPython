'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(ano):
    from datetime import date
    print('-' * 30)
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, NÃO PODE VOTAR.'
    elif idade < 18 and idade >= 16 or idade > 65:
        return f'Com {idade} anos, VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))

