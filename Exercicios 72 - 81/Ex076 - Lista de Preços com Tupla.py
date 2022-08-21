# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

t = ('Lapis', 1.75,
     'Borracha', 2,
     'Caderno', 15.90,
     'Estojo', 25,
     'Transferidor', 4.20,
     'compasso', 9.99,
     'Mochila', 120.32,
     'Canetas', 22.30,
     'Livro', 34.90)
print('-' * 53)
print('{: ^53}'.format('LISTAGEM DE PREÇOS'))
print('-' * 53)
for c in range(0, len(t)):
    if c % 2 == 0:
        print('{0:.<40}'.format(t[c]), end='  ')
    else:
        print('R${0: >8.2f}'.format(t[c]))
print('-' * 53)