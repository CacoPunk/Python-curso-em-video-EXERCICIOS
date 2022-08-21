#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um valor: '))
escolha = int(input('Digite 1 para converter em binario, 2 para octal e 3 para hexadecila: '))
if escolha == 1:
    print('O numero {} em binario é: {}'.format(num, bin(num)))
elif escolha == 2:
    print(('O numero {} em octal é: {}'.format(num, oct(num))))
elif escolha == 3:
    print('O numero {} em hexadecimal é {}'.format(num, hex(num)))
else:
    print('Desculpe valor escolhido invalido')

