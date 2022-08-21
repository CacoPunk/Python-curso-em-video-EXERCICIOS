#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você rodou com o carro? '))
#a = dias * 60
#b = km * 0.15
#valor = a + b
valor = (dias *60 ) + (km * 0.15)
print('Valor total do do aluguel R${:.2f}'.format(valor))
