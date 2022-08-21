def metade(n=0, m=True):
    return n / 2 if m is False else moeda(n / 2)


def dobro(n=0, m=True):
    return n * 2 if m is False else moeda(n * 2)


def aumentar(n=0, p=0, m=True):
    porc = n + (n * p) / 100
    return porc if m is False else moeda(porc)


def diminuir(n =0, p=0, m=True):
    porc = n -(n * p) / 100
    return porc if m is False else moeda(porc)


def moeda(n=0, moeda ='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

def resumo(num=0, aum=0, dim=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<18} {moeda(num):>11}')
    print(f'{"Dobro do preço:":<18} {dobro(num):>11}')
    print(f'{"Metade do preço":<18} {metade(num):>11}')
    print(f'{f"{aum}% de aumento":<18} {aumentar(num, aum):>11}')
    print(f'{f"{dim}% de redução":<18} {diminuir(num, dim):>11}')
    print('-' * 30)