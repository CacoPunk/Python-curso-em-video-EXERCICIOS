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


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (KeyboardInterrupt):
            print('\nUsuario preferiu nao digitar esse valor')
            return 0
        except:
            print('ERRO! Por favor digite um numero Real.')
            continue
        else:
            return num

def acessivelURL(url):
    import urllib
    import urllib.request
    try:
        site1 = urllib.request.urlopen(url)
    except urllib.request.URLError:
        print('O Site não está acessível no momento')
    except:
        print('Endereço invalido ')
    else:
        print('Consegui abrir o site com sucesso!')