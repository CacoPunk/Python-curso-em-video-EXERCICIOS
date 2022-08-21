#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

anoa = date.today().year

maior = 0
menor = 0
for c in range(1,8):
        ano = int(input('Em que anoa {}a pessoa nasceu? '.format(c)))
        if anoa - ano < 18:
            menor += 1
        else:
            maior += 1
print('''Ao todo temos {} pessoas maiores de idade
E tambem {} pessoas menores de idade'''.format(maior, menor))
