# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    while True:
        cond =  input('Quer continuar? [S/N]').strip().upper()
        if cond == 'S' or cond == 'N':
            break
    if cond == 'N':
        break
lista.sort()
print(f'{lista}')
