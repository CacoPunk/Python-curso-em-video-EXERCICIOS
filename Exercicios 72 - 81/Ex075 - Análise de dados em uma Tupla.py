#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
par = 0
t = (int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')))
for c in range(0, len(t)):
  if t[c] % 2 == 0:
      par += 1
print(f'Você digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)}', end=' ')
print('vez' if t.count(9) == 1 else 'Vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3, 0)+1}ªposição')
else:
    print(f'O valor 3 não apareceu em nenhuma pocição')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores pares digitados foram ',end=' ')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')