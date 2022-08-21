# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nomes = []
idades = []
sexos = []
somaidade = 0
hvelho = 0
homem = ''
mulheres = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]').strip().upper()
    somaidade += idade
    if sexo == 'M':
        if idade > hvelho:
            hvelho += idade
            homem = nome
    elif sexo in 'Ff'and idade < 20:
            mulheres += 1
print('A media de idade do grupo é {} anos.'.format(somaidade / 4))
print('O nome do homem mais velho é: {}'.format(homem))
print('A quantidade de mulheres com menos de 20 anos é: {} '.format(mulheres))