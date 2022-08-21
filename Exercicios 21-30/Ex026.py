# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A letra a aparece pela primeira vez na pocição {} '.format(frase.find('A')+1))
print('A letra a aparece pela ultima vez na pocição {} '.format(frase.rfind('A')+1))
print(len(frase))