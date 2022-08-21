#Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto:'))
cond = int(input('Agora escolha a forma de pagamento.\nDIGITE:\n[1] Para pagamento à vista dinheiro/cheque;\n'
                 '[2] Para pagamento à vista no cartão.\n[3] Para parcelar em 2x no cartão.\n'
                 '[4]Parcelar em 3x ou mais no cartão.\n'))
if cond == 1:
    print('Você terá um desconto de 10% e pagara R${}.'.format(preco - (preco * 10/100)))
elif cond == 2:
    print('Você terá um desconto de 5% e pagara R${}.'.format(preco - (preco * 5 / 100)))
elif cond == 3:
    print('Você pagara o valor formal R${}'.format(preco))
elif cond == 4:
    parc = int(input('Em quantas vezes você deseja parcelar? '))
    total = preco + (preco * 20 / 100)
    vparc = total / parc
    print('Você terá um acrescimo de 20% e pagara um total de R${}, em {}x de R${}.'.format(total, parc, vparc))

