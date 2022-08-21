#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contador(ini, fim, passo):
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if passo <0:
        passo *= -1
    if passo == 0:
         passo = 1
    if ini <= fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ', flush=False)
            sleep(.3)
            cont += passo
        print('FIM!')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ',flush=False)
            sleep(.3)
            cont -= passo
        print('FIM!')

contador(0, 10, 1)
print()
contador(10, 0, 2)
inicio = int(input('Digite o Inicio: '))
final = int(input('Digite o final: '))
passo = int(input('Digite o passo: '))
contador(inicio, final, passo)