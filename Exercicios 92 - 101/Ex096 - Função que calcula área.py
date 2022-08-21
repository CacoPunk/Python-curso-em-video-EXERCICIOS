# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def área(a, b):
    a = a * b
    print(f'A area total de um terreno {a}x{b} é {a}m²')

larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
área(larg, comp)
