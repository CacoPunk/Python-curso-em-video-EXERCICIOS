#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso

print(maior)
print(menor)
