num = [2, 5, 9, 1]
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.sort()
print(num)
print(len(num))
num.insert(2, 8)
print(num)
num.pop(2)
print(num)
if 5 in num:
    num.remove(5)
print(num)
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
