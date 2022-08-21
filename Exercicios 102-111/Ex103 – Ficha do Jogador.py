# Faça um programa que tenha uma função chamada ficha(), q
# ue receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(a=0, b=0):
    if a == '':
        a = '<desconhecido>'
    try:
        int(b)
    except:
        b = 0
    print(f'O jogador {a} fez {b} gol(s).')

#programa principal
nome = input('Nome do jogador: ')
gols = input('Numero de gols: ')
ficha(nome, gols)