#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 30)
print("{:^30}".format('BANCO DO CACO'))
print('=' * 30)
sac = int(input('Quanto você deseja sacar? R$'))
n20 = n50 = n10 = n1 = 0
if sac >= 50:
     n50 = sac // 50
     sac = sac % 50
if sac >= 20:
    n20 = sac // 20
    sac = sac % 20
if sac >= 10:
    n10 = sac // 10
    sac = sac % 10
if sac >= 1:
    n1 = sac // 1
    sac = sac % 1
print(n50)
print(n20)
print(n10)
print(n1)
print(sac)