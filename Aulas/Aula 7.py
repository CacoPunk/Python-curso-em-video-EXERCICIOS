#nome = input('Qual é seu nome?')
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:-^20}!'.format(nome))

n1 = int(input('Um Valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
sd = n1 % n2
e = n1 ** n2
print('A soma é {},\n o produto é {}\n e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('Divisão inteira{}, Sobra{} e a potencia {}.'.format(di, sd, e))