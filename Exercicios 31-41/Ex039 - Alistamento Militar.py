# # Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

ano = date.today().year

nasc = int(input('Digite o ano que você nasceu: '))
idade = ano - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))
if idade < 18:
    print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('No ano de {}'.format(nasc + 18))
elif idade > 18:
    print('Voce deveria ter se alistado a {} anos'.format(idade - 18))
    print('Em {}'.format(ano - (idade - 18)))
else:
    print('Atenção voce deve se alistar IMEDIATAMENTE')