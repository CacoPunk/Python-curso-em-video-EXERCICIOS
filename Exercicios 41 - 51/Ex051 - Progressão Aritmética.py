# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('    10 TERMOS DE UMA PA    ')
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print('{} '.format(p),end='-> ')
    p += r
print('ACABOU')