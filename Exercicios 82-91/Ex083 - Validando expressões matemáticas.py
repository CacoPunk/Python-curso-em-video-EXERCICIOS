#083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = str(input('Digite  a expressão: '))
abr = exp.count('(')
fec = exp.count(')')
if abr == fec:
    print('Sua expressão está correta.')
else:
    print("Sua expressão está errada.")