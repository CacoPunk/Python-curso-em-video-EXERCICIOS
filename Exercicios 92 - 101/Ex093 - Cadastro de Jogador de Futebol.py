#093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
totgols = 0
fut = {}
numgols = []
fut['Nome'] = input('Nome do Jogador: ')
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(0, partidas):
    numgols.append(int(input(f'Quantos gols ele fez na partida {c+1} ')))
fut['Gols'] = numgols[:]
for c in numgols:
    totgols += c
fut['Total'] = totgols
print('-='*30)
print(fut)
print('-='*30)
for k, v in fut.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {fut["Nome"]} jogou {partidas} partidas.')
for a, b in enumerate(fut['Gols']):
    print(f' => Na partida {a+1}, fez {b} gols.')
print(f'Foi um total de {fut["Total"]} gols')