# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Qual digite seu salario: '))
if s > 1250:
    sa = s * 10 / 100 + s
else:
    sa = s * 15 / 100 + s
print(sa)

