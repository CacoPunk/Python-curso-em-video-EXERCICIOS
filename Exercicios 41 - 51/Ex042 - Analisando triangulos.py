#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

r1 = float(input('Digite o valor de um lado do triangulo '))
r2 = float(input('Digite o valor de um lado do triangulo '))
r3 = float(input('Digite o valor de um lado do triangulo '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('Esses valores PODEM formar um triangulo EQUILATERO')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Esses valores podem formar um triangulo ESCALENO')
    else:
        print('Eses valores podem formar um triangulo ISÓCELES')
else:
    print('Esses valores NÂO podem formar um triangulo')
