''''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

from math import factorial
print('FATORIAL AUTOMATICO.')
n = int(input('Digite um numero: '))
if n < 0:
    print('Fatorial negativo não existe')
else:
    t = factorial(n)
    print('Calculando {} = '.format((n)),end='')
    print('{}'.format(n),end='')
    while n > 1:
        n -= 1
        n2 = n - 1
        print(' x {}'.format(n),end='')
    print(' = {}'.format(t))

