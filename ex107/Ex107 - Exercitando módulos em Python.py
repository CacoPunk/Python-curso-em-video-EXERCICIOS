#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from ex107 import moeda as md

num = int(input('Digite um valor R$'))
print(f'A metade de {num} é {md.metade(num)}')
print(f'O dobro de {num} é {md.dobro(num)}')
print(f'aumentando 10%, temos {md.aumentar(num, 10)}')
print(f'Diminuindo 15%, temos {md.diminuir(num, 15)}')