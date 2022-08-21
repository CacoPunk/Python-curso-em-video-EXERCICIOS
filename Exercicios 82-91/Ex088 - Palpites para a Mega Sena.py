#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

jogo = list()
temp = 0
print('-'*30)
print('{:^30}'.format('GERADOR MEGA SENA!'))
print('-'*30)

cont = int(input('Quantos jogos eu devo sortear? '))
print('-='*3, end='   ')
print(f'SORTEANDO {cont} jogos', end='   ')
print('-='*3)
for c in range(1, cont + 1):
    sleep(0.5)
    while len(jogo) < 6:
        temp = randint(1, 60)
        if temp not in jogo:
            jogo.append(temp)
        jogo.sort()
    print(f'Jogo {c}: {jogo}')
    jogo.clear()