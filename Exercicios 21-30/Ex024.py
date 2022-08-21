#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade em que você nasceu: ')).strip()
a = cidade.lower().split()
print('santo' in a[0])

#maneira que o professor resolveu

print(cidade[:5].upper() == 'SANTO')

#outra maneira

#cidade = str(input('Digite uma cidade: ')).upper().strip().split()
#print('Essa cidade começa com SANTO? {}'.format('SANTO' in cidade[0]))
