#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
dic = {}
dic['nome'] = input('Nome: ')
dic['média'] = int(input(f'Média de {dic["nome"]} '))
if dic['média'] >= 7:
    dic['situação'] = 'Aprovado'
elif dic['média'] >= 5:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
for k, v in dic.items():
    print(f' - {k} é igual a {v}')