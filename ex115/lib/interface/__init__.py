def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (KeyboardInterrupt):
            print('\nUsuario preferiu nao digitar esse valor')
            return 0
        except:
            print('Erro! Por favor digite um numero inteiro! ')
            continue  # ESSE COMANDO VOLTA PRO INICIO DO LAÇo
        else:
            return num


def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))



def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
    print(linha())
    opc = leiaint('Escolha uma opção: ')
    return opc
