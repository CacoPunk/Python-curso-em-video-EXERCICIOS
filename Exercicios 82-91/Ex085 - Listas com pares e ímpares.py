lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}o valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[1].sort()
lista[0].sort()
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores impares são: {lista[1]}')