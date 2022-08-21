#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
lista = []
som = 0
for c in range(0, 6):
    num = int(input('Digite um numero: '))
    lista.insert(c, num)
for b in range(0, 6):
    if lista[b] % 2 == 0:
        som = som + lista[b]
print(som)