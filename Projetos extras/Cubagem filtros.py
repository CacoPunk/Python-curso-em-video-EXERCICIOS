cubf = 0
c = float(input('Digite a largura do veiculo: (m) '))
d = float(input('Digite a altura do veiculo: (m) '))
e = float(input('Digite o comprimento do veiculo: (m) '))
cubv = c * d * e
while True:
    c = (float(input('Digite a largura do filtro: (mm) ')) / 1000)
    d = (float(input('Digite o comprimento do filtro: (mm) ')) / 1000)
    e = (float(input('Digite a altura do filtro: (mm) ')) / 1000)
    n = int(input('Quantidade: '))
    cub = (c * d * e) * n
    cubf += cub
    z = int(input('Continuar?[1/0]'))
    if z == 0:
        break
print(f'O veiculo tem capacidade de {cubv}m³.')
print(f'Os filtros vão ocupar {cubf}m³.')
