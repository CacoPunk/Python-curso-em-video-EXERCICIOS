# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6

import math
num = float(input('Digite um numero real'))
print('Numero real {} . numero truncado {}'.format(num, math.floor(num)))#tambem funciona com a função trunc
#tambem funciona com int(num) sem importar nada.
