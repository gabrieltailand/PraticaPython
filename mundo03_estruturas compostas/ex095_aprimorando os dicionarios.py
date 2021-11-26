'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''

dados = dict()
partidas = list()
time = list()
# Leitura dos dados
while True:
    dados.clear()
    dados['jogador'] = str(input('Digite o nome do jogador: '))
    tot_partidas = int(input(f'Número de partidas jogadas de {dados["jogador"]}: '))
    partidas.clear()
    for c in range(0, tot_partidas):
        partidas.append(int(input(f'Número de gols na {c+1}ª partida: ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp in 'N':
        break
# Mostrar os resultados
print('-' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
# Vizualização de aproveitamento
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}')
    else:
        print(f' -- ANÁLISE DO JOGADOR {time[busca]["nome"]}') # ANÁLISE DO JOGADOR {time[busca]["nome"]}') - erro

