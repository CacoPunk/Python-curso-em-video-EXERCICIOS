#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Digite a temperatura em ºC: '))
far = (cel * 9 / 5 ) + 32
print('{}ºC equivalem a {:.2f} Fahrenheit.'.format(cel, far))