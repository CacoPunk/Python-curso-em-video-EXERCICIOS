# nome = str(input('Qual seu nome: '))
# if nome == 'Gustavo':
#    print('que nome lindo')
# else:
#    print('Seu nome é normal')
# print('Bom dia {}'.format(nome))

n1 = float(input('Nota 1: '))
n2 = float(input('nota2: '))
media = (n1 + n2) / 2
if media >=6:
    print('Aprovado nota{:.2f}'.format(media))
else:
    print('Recuperação nota{:.2f}'.format(media))
