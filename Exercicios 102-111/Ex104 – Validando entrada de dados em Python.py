#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def LeiaInt(txt):
    while True:
        x = input(txt)
        if x.isnumeric():
           valor = int(x)
           break
        else:
            print('ERRO! Digite um numero valido')
    return(valor)

#PROGRAMA PRINCIPAL
n = LeiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}.')