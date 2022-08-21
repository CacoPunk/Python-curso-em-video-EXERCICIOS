#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = dict()
lista = list()
idades = media = 0
while True:
    pessoas['nome'] = input('Nome: ')
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo == 'M' or sexo == 'F':
            pessoas['sexo'] = sexo
            break
        else:
            print('ERRO! Por favor digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    while True:
        cond = input('Quer continuar? [S/N] ').strip().upper()
        if cond == 'S' or cond == 'N':
            break
        else:
            print('ERRO! Responda S ou N!')
    lista.append(pessoas.copy())
    if cond == 'N':
        break
    pessoas.clear()
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for c in range(0, len(lista)):
    idades += lista[c]['idade']
media = idades / len(lista)
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram: ',end='')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(lista[c]['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for c in range(0, len(lista)):
    if lista[c]['idade'] > media:
        print(f'  nome = {lista[c]["nome"]}; sexo = {lista[c]["sexo"]}; idade = {lista[c]["idade"]}')
print(lista)