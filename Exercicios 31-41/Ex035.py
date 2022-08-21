# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o valor de um lado do triangulo'))
r2 = float(input('Digite o valor de um lado do triangulo'))
r3 = float(input('Digite o valor de um lado do triangulo'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Esses valores PODEM formar um triangulo')
else:
    print('Esses valores NÂO podem formar um triangulo')
