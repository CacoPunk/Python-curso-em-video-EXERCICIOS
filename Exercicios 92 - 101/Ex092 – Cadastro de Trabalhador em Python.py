# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
func = {}
func['Nome'] = input('Nome: ')
ano = datetime.today().year
ano2 = int(input('Ano de nascimento: '))
func['Idade'] = ano - ano2
ctps = int(input('Carteira de Trabalho: (0 não tem) '))
if ctps > 0:
    func['Ctps'] = ctps
    func['Contratação'] = int(input('Ano da Contratação: '))
    func['Salário'] = float(input('Salário: '))
    func['Aposentadoria'] = (func['Contratação'] + 35) - ano2
else:
    func['Ctps'] = ctps
print('-='*30)
for k, v in func.items():
    print(f' - {k} tem o valor {v}')