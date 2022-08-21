# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        c = input('Quer continuar? [S/N] ').strip().upper()
        if c == 'S' or c == 'N':
            break
    if c == 'N':
         break
lista.sort(reverse=True)
print('--'*20)
print(f'Foram digitados {len(lista)} valores!')
print('--'*20)
print(lista)
print('--'*20)
if 5 in lista:
    print('Numero 5 está na lista')
else:
    print('Numero 5 não está na lista')
print('--' * 20)