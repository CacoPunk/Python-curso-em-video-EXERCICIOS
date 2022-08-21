#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
a = b = c = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Erro, informe novamente.')
    if idade > 18:
        a += 1
    if sexo == 'M':
        b += 1
    if sexo == 'F' and idade < 20:
        c += 1
    while True:
        print('-' * 20)
        cond = input('Qeer contuniar? [S/N] ').strip().upper()
        if cond == 'S' or cond == 'N':
            break
        else:
            print('Erro, informe novamente.')
    if cond == 'N':
        break
print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {a}')
print(f'Ao todo temos {b} homens cadastrados.')
print(f'Temos {c} mulheres com menos de 20 anos')
print('FIM')
