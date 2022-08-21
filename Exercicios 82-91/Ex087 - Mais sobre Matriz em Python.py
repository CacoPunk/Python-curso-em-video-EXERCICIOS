# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[], [], []]
somap = somatc = maior = 0
for c in range(0, len(matriz)):
    for x in range(0, 3):
        matriz[c].append(int(input(f'Digite o valor de: [{c}, {x}]: ')))
for c in range(0, len(matriz)):
    for x in range(0, 3):
        print(f'[{matriz[c][x]:^5}]', end='')
    print()
for c in range(0, len(matriz)):
    for x in range(0, 3):
        if matriz[c][x] % 2 == 0:
            somap += matriz[c][x]
for c in range(0, 3):
    somatc += matriz[c][2]
print(f'A soma dos valores pares é {somap}.')
print(f'A seoma dos valores da terceira coluna é: {somatc}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')