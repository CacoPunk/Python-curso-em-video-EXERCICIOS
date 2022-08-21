print('**' * 20)
print('GERADOR DE TABUADA By: DEV ser o CACO.')
print('**' * 20)
while True:
    num = int(input('Quer ver a taboada de qual valor? '))
    print('**' * 20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('**' * 20)
print('Programa encerrado. Espero que tenha gostado.')