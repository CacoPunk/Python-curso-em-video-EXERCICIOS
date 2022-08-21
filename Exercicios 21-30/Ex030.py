#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um numero e vou descobrir se é par ou impar: '))
x = n % 2
if x == 0:
    print('Descobri que {} é um numero par'.format(n))
else:
    print('Descobri que {} é um numero impar'.format(n))
