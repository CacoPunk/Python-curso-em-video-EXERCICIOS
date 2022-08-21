def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro: \"{entrada}\"  um preço invalido')
        else:
            valido = True
            return float(entrada)


def LeiaInt(txt):
    while True:
        x = input(txt)
        if x.isnumeric():
           valor = int(x)
           break
        else:
            print('ERRO! Digite um numero valido')
    return(valor)
