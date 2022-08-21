#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
t = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: ',end='')
menor = maior = 0
for n in t:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi: {max(t)}')
print(f'O menor valor sorteado foi: {min(t)}')
