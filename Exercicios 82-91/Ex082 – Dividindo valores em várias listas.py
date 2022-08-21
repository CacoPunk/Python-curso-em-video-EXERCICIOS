#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = limpar = lpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        cond = input('Quer continuar? [S/N] ').strip().upper()
        if cond == 'S' or cond == 'N':
            break
    if cond == 'N':
        break
for c, v in enumerate(lista):
    if lista[c] % 2 == 0:
        lpar.append(lista[c])
    else:
        limpar.append((lista[c]))
print(('*-' * 10))
print(f'A lista de numeros é: {lista}')
print(('*-' * 10))
print(f'A lista de numeros pares é: {lpar}')
print(('*-' * 10))
print(f'A lista de numeros impares é: {limpar}')
print(('*-' * 10))