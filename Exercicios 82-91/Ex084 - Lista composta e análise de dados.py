#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
# mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
pessoas = list()
dados = list()
pesados = list()
leves = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        cond = input('Quer continuar? [S/N] ').strip().upper()
        if cond == 'S' or cond == 'N':
            break
    if cond == 'N':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior pesso cadastrado é {maior}kg. ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor pesso cadastrado é {menor}kg. ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')