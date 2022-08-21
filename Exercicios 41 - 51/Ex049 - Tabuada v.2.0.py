#Refaça o DESAFIO 9, mo5strando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um numero de 1 a 9 para ver a tabuada do mesmo: '))
if num <=9:
    for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, num * c))
else:
    print('Valor invalido.')