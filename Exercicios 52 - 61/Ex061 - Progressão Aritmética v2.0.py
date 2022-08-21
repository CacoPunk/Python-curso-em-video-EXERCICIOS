#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.


print('=' * 30)
print('    10 TERMOS DE UMA PA    ')
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = int(input('Quantos termos deseja vizualizar? '))
while t > 0:
    print('{} '.format(p),end='-> ')
    p += r
    t -= 1
print('ACABOU')