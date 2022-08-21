#102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a cal
# cular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
def fatorial(n, show=False):
    from math import factorial
    t = factorial(n)
    if show:
        print(f'{n} x ', end='')
        while n > 1:
            n -= 1
            print(f'{n} ', end='')
            print('x ' if n > 1 else '= ', end='')
    return (t)

print(fatorial(6, True))