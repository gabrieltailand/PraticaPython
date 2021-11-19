'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Cotinthias', 'Fortaleza', 'Internacional', 'Fluminense',
          'América-MG', 'Ceará', 'Santos', 'Cuibá', 'Athletico-PR', 'São Paulo', 'Juventude', 'Atlético-GO', 'Bahia',
          'Sport', 'Grêmio', 'Chapecoense')
import random
print(f'\033[34mOs cincos primeiros colocados são:\033[m {tabela[0:5]}')
print('-' * 105)
print(f'\033[34mO ultimos quatro colocados são:\033[m {tabela[16:]}')
print('-' * 105)
ordem = sorted(tabela)
print(f'\033[34mOs times em ordem alfabética são:\033[m\n{ordem}')
print('-' * 105)
print(f'\033[34mO time da Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição.')


