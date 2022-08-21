#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 30)
print('    10 TERMOS DE UMA PA    ')
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = int(input('Quantos termos deseja vizualizar? '))
a = True
cont = 0
while a == True:
    while t > 0:
        print('{} '.format(p),end='-> ')
        p += r
        t -= 1
        cont += 1
    print('PAUSA')
    x = int(input('Quantos termos a mais você deseja mostrar? '))
    if x == 0:
        a = False
    else:
        t = x
print('PA finalizada {} termos mostrados'.format(cont))
print('ACABOU')