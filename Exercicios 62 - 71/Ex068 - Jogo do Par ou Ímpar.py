# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
cont = 0
from random import randint
print('=-=' * 13)
print('Jogo par ou impar! By: DEV ser o CACO.')
print('=-=' * 13)
while True:
    while True:
        escolha = input('Par ou Impar? [P/I] ').strip().upper()
        if escolha == 'P' or escolha == 'I':
            break
        else:
            print('Escolha invalida.')
    com = randint(0, 10)
    play = int(input('Escolha seu valor: '))
    x = (play + com) % 2
    if x == 0:
        res = 'DEU PAR'
    else:
        res = 'DEU IMPAR'
    print('--' * 28)
    print(f'Você jogou {play} e o computador {com}. Total de {play + com} {res}')
    print('--' * 28)
    if escolha == 'I' and x == 0:
        print('Você perdeu!')
        break
    elif escolha == 'I' and x != 0:
        print('Você ganhou!')
        cont += 1
    elif escolha == 'P' and x == 0:
        print('Você ganhou!')
        cont += 1
    elif escolha == 'P' and x != 0:
        print('Você perdeu!')
        break
print('=-=' * 13)
print(f'Game over. Você ganhou {cont} vezes!')