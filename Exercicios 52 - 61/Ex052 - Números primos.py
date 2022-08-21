#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

n = int(input('Digite um numero: '))
b = 0
for c in range(1, n+1):
    if n % c == 0:
        b += 1
        print(bcolors.OK + '{}'.format(c), end=' ' + bcolors.RESET)
    else:
        print(bcolors.FAIL + '{}'.format(c), end=' ' + bcolors.RESET)
print('\n')
print('O numero {} foi divisível {} vezes, então: '.format(n, b))
if b == 2:
    print('Numero primo')
else:
    print('Não primo')
