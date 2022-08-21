#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
a = b = c= cont = 0
c1 = ' '
print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATO'))
print('-'*30)
while True:
    cont = + 1
    nome = input('Nome do produto: ')
    valor = float(input('Valor do produto: R$'))
    while True:
        cond = input('Quer cadastrar mais um produto? [S/N] ').strip().upper()
        if cond == 'N' or cond == 'S':
            break
    a += valor ###aqui  resolvemos o A
    if valor >= 1000:###Aqui resolvemos o B
        b +=1
    if cont == 1 or valor < c:
            c = valor
            c1 = nome
    if cond == 'N':
        break
print('{:-^30}'.format('Fim'))
print(f'O total da compra foi R${a:.2f}.')
print(f'Temos {b} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato é a {c1} que custa R${c:.2f}.')
print('{:-^30}'.format('Fim'))
