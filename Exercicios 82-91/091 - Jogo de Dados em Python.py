#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jog = {}
rank = {}
for c in range(1, 5):
    jog[f'jogador{c}'] = randint(1, 6)
for k, v in jog.items():
    print(f'{k} tirou {v}')
    sleep(.5)
rank = sorted(jog.items(), key=itemgetter(1), reverse=True)#coloca em uma lista na ordem desejada
for i, v in enumerate(rank):
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')
    sleep(.5)