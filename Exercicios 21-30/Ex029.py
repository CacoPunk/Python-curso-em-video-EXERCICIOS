#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vl = int(input('Digite a velocidade do carro: '))
if vl <= 80:
    print('Veiculo dentro do limite!')
else:
    rv = vl - 80
    print('Você estava {}km/h acima do limite'.format(rv))
    print('Você sera multado em R${}'.format(rv * 7))
    
