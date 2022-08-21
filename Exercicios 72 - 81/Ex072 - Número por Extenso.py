num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
       n = int(input('Digite um numero entre 0 e 20: '))
       if n >= 0 and n <= 20:
              break
print(f'Você digitou o numero {num[n]}')
