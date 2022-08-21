# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

palavra = str(input('Digite uma frase: ')).strip()
print(palavra.upper())
print(palavra.lower())
print(len(palavra) - palavra.count(' '))
print(palavra.find(' '))
separa = palavra.split()
print(separa)
print(len(separa[0]))
print(len(separa[1]))
print(len(separa[2]))