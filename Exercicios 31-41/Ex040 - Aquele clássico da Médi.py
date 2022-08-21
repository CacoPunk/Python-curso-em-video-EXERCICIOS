# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print('Média do aluno: {}'.format(med))
if med < 5:
    print('Você está reprovado.')
elif med >= 5 and med < 7:
    print(('Você esta em recuperação.'))
else:
    print('Voce está aprovado.')
