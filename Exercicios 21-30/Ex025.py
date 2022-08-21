# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome: ')).strip().lower()
print('Tem a palavra santo no seu nome? {}'.format('silva'in nome))
