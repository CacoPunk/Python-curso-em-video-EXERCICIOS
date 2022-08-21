# Exercício Python 018: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang1 = float(input('Digite o ângulo desejado: '))
ang = math.radians(ang1)# é necessario passar o valor em º para radianos antes de usar sin, cos e tan
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang1, sen))
print('O ângulo de {} tem o COSSENO de{:.2f}'.format(ang1, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang1, tan))