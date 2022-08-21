# Exercício Python 017: Faça um programa que leia o comprimento do
# cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# from math import sqrt  - pegar apeanas a raiz quadrada

import math

co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
# h = sqrt(pow(co, 2)+pow(ca, 2))
# h = (co ** 2 + ca ** 2) ** (1/2)
h = math.hypot(co, ca)
print('A hipotenusa vale: {:.2f}'.format(h))
