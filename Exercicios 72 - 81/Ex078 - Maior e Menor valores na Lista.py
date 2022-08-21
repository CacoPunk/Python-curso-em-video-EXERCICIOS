#078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior = menor = x = 0
for d in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {d}: ')))
for c, v in enumerate(lista):
    if c == 0:
        maior = menor = v
    elif v > maior:
        maior = v
    elif v < menor:
        menor = v
print(f'Você digitou: {lista}')
print(f'O maior valor digitado foi {maior} nas pocições: ',end='')
for i, u in enumerate(lista):
    if u == maior:
        print(f'{i}... ',end='')
print(f'\nO menor valor digitado foi {menor} nas pocições: ',end='')
for i, u in enumerate(lista):
    if u == menor:
        print(f'{i}... ',end='')