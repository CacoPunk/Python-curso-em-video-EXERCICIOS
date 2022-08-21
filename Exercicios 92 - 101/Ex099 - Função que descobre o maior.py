#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep
def maior(*val):
    print('-='*30)
    print('Analisando valores')
    sleep(.5)
    for c in val:
        print(c, end=' ')
        sleep(.5)
    print(f'Foram informandos {len(val)} valores ao todo.')
    sleep(.5)
    print(f'O maior valor informado foi {max(val)}')
    sleep(.5)

#programa principal
lista = list()
for x in range(0, randint(0, 10)):
    for c in range(0, randint(1, 10)):
        lista.append(randint(0, 10))
    maior(lista)
   lista.clear()
#maior(1,3,5,7,4,2,4)
#maior(0)