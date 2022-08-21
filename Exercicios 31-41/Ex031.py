#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual a distancia em KM da viagem? '))
if km <= 200:
    print('Esta viagem vai lhe custar R${}'.format(km * 0.50))
else:
    print('Esta viagem vai lhe custar R${}'.format(km * 0.45))
