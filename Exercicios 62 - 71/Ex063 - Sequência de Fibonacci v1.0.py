# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de um
# Sequência de Fibonacci. Exemplo:
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

f1 = 0
f2 = 1
x = int(input('Quantos termos você deseja mostrar? '))
for c in range(0, x):
    print(f1,end=' -> ')
    fn = f1 + f2
    f1 = f2
    f2 = fn
print('FIM')
5
