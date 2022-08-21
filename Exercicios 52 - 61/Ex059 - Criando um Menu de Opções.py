'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''


from time import sleep
c = True
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o seguindo valor: '))
while c == True:
    print('''    [1] somar   
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    m = int(input('>>>>Escolha uma opçao: '))
    if m == 1:
        print('A soma entre {} e {} é: {}: '.format(n1, n2, (n1 + n2)))
    elif m == 2:
        print('A multiplicação entre {} e {} é: {}: '.format(n1, n2, (n1 * n2)))
    elif m == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}.'.format(n2, n1))
        else:
            print('Os valores são iguais.')
    elif m == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o seguindo valor: '))
    elif m == 5:
        c = False
    else:
        print('Opção invalida')
    print('*=*' * 10)
    sleep(1.5)
print('Muito obrigado por utilizar eu software!')
