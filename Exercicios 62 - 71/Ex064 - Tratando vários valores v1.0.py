# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).,

a = 0
num = 0
cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar] ')) #TAMBEM DA Para colocar esse input do lado de fora do laço e depoois no final do while.
    if num != 999:
        a += num
        cont += 1
print('Você digitou {} números e a soma entre eles é {}'.format(cont, a))
