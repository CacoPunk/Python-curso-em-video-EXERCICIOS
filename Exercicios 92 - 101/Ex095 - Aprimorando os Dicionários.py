#Aprimore o desafio 93 para que ele funcione com vários jogadores
# , incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
totgols = 0
lista = []
fut = {}
numgols = []
cont = 0
while True:
    fut.clear()
    fut['Nome'] = input('Nome do Jogador: ')
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(0, partidas):
        numgols.append(int(input(f'Quantos gols ele fez na partida {c+1} ')))
    fut['Gols'] = numgols[:]
    for c in numgols:
        totgols += c
    fut['Total'] = totgols
    while True:
        cond = input('Quer continuar? [S/N] ').strip().upper()
        if cond == 'S' or cond == 'N':
            break
    lista.append(fut.copy())
    numgols.clear()
    totgols = 0
    if cond == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in fut.keys():
    print(f'{i:<15}',end='')
print()
print('-'*45)
for k, v in enumerate(lista):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15} ',end=' ')
    print()
print('-'*45)
while True:
    con2 = int(input('Mostrar dados de qual jogar? (999 para parar) '))
    if con2 == 999:
        break
    elif con2 >= len(lista):
        print(f'ERRO! Não existe jogador com codigo {con2}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[con2]["Nome"]}')
        for a, b in enumerate(lista[con2]['Gols']):
            print(f' => Na partida {a + 1}, fez {b} gols.')
        print(f'Foi um total de {lista[con2]["Total"]} gols')
    print('-' * 45)
print(lista)