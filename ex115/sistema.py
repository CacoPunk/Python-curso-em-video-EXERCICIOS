from ex115.lib.interface import  *
from ex115.lib.arquiv import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    crarArquivo(arq)
lista1 = ['Ver pessoas cadastradas.', 'Cadastrar pessoas', 'Sair do sistema']

while True:
    resposta = menu(lista1)
    if resposta == 1:
        print(cabeçalho(lista1[resposta-1]))
        lerArquivo(arq)
    elif resposta == 2:
        print(cabeçalho(lista1[resposta-1]))
    elif resposta == 3:
        print(cabeçalho(lista1[resposta-1]))
    else:
        print('ERRO! DIGITE UMA OPLÇÃO VALIDA.')
    sleep(1.5)