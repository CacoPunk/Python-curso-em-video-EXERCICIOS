#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
print('-'*30)
print('{:^30}'.format('BRASILEIRÃO SERIE A'))
print('-'*30)
times = ('Corinthians', 'Bragantino', 'Atltético-MG', 'Coritiba', 'São Paulo', 'Santos', 'Cuiabá', 'Internacional',
         'Avaí', 'América-MG', 'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará SC', 'Athletico-PR',
         'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
a = times.index('Juventude')
print(f'Esses são os times na classificação atual: {times}')
print('-'*80)
print(f'Esses são os 5 primeiros colocados{times[0:5]}')
print('-'*80)
print(f'Esses são os ultimos 4 colocados: {times[-4:]}')
print('-'*80)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-'*80)
print(f'Essa é a posiçao do JUZÃO: {a+1}º')
print('-'*80)