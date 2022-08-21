# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.
a = True
cont = soma = maior = 0
menor = 0
while a == True:
    num = int(input('Digite um numero: '))
    cond = input('Quer continuar? [S/N]').strip().upper()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while cond != 'S' and cond != 'N':
        print('Resposta invalida')
        cond = input('Quer continuar? [S/N]').strip().upper()
    if cond == 'N':
        a = False
media = soma / cont
print('Voce digitou {} valores, a média desses valores é de {}, o maior valor digitado é {} e o menor é {}'.format(cont, media, maior, menor))