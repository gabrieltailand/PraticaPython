'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dados = dict()
partidas = list()

dados['jogador'] = str(input('Digite o nome do jogador: '))
tot_partidas = int(input(f'Número de partidas jogadas de {dados["jogador"]}: '))

for c in range(0, tot_partidas):
    partidas.append(int(input(f'Número de gols na {c+1}ª partida: ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)

print('-' * 30)
print(dados)
print('-' * 30)

for k, v in dados.items(): # Usar items para dicionários.
    print(f'O campo {k} tem o valor {v}.')
print('-' * 30)
print(f'O jogador {dados["jogador"]} jogou {tot_partidas} partidas.')
for i, v in enumerate(dados['gols']): # Usar enumerate para listas.
    print(f' - Na partida {i+1} fez {v} gols.')
print(f'Total de {dados["total"]} gols.')




