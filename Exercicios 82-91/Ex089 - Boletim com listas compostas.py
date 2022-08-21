# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.
aluno = list()
lista = list()
while True:
    aluno.append(input('Nome: '))
    aluno.append(int(input('Nota 1: ')))
    aluno.append(int(input('Nota 2: ')))
    lista.append(aluno[:])
    aluno.clear()
    while True:
        cond = input('Quer continuar? [S/N] ').strip().upper()
        if cond == 'S' or cond == 'N':
            break
    if cond == 'N':
        break
print('-='*30)
print('{:<4}'.format('No.'), '{:<12}'.format('Nome'), '{:>5}'.format(('MÉDIA')))
print('-'*21)
for c in range(0, len(lista)):
    print('{:<4}'.format(c), '{:<12}'.format(lista[c][0]), '{:>5.2f}'.format((lista[c][1] + lista[c][2]) / 2))
print('-'*21)
while True:
    cond2 = int(input(('Deseja ver aa notas de qual aluno?(999 interrompe) ')))
    if cond2 == 999:
        break
    elif cond2 <= len(lista):
        print(lista[cond2][1][2])