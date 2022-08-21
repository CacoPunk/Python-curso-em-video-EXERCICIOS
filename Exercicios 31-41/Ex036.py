#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('-' * 40)
print('Simulador de empréstimo.')
print('-' * 40)

v1 = float(input('Digite o valor do imóvel: '))
v2 = float(input('Qual sua renda mensal?'))
v3 = int(input('Informe em quantos anos você deseja parcelar:'))
vmax = v2 * 30 / 100
nump = v3 * 12
vpar = v1 / nump

print('Você deseja parcelar em {}x de R${:.2f}'.format(nump, vpar))
if vpar <= vmax:
    print('Parabéns seu emprestimo foi aprovado')
else:
    print('Sinto muito mas o valor da parcela ultrapassa 30% do seu salario.')
