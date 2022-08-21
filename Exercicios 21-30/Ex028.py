#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

print(':-:' * 20)
print('Vou Pensar em um numero entre 0 e 5. Tente Adivinhar...')
print(':-:' * 20)
n = int(random.randrange(0, 6)) # pode ser randint(0, 5)
print('***' * 20)
n2 = int(input('Digite o numero: '))
print('***' * 20)
if n2 == n:
    print('Você ganhou')
else:
    print('Eu ganhei otario {}'.format(n))