# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

pc = randint(0, 2)
lista = ['pedra', 'papel', 'tesoura']
print('+=+=' * 6)
print('+=+=JO.KEN.PO GAME!!+=+=')
print('+=+=' * 6)
print('[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
jog = int(input('Qual sua jogada?\n '))
if jog < 3:
      sleep(1)
      print('JOOO')
      sleep(1)
      print(('KENNN'))
      sleep(1)
      print('POOOOOO!!!!')
      sleep(1)
      p = lista[jog]
      c = lista[pc]
      print('*-*' * 10)
      print('Voce escolheu {}!\nPC escolheu {}!'.format(p, c))
      print('*-*' * 10)

      if jog == pc:
            print('EMPATE')
      elif (jog == 0 and pc == 2) or (jog == 1 and pc == 0) or (jog == 2 and pc == 1):
            print('Vitoria')
      else:
            print('Derrota')
else:
      print('Jogada invalida')
