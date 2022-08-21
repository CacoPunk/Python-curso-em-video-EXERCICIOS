#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
#datetime.today().year
from datetime import datetime
def voto(nasc):
    """
    Descobre atraves do ano de nascimento se o voto é opcional ou obrigatorio
    :param nasc: data de nascimento 
    :return: Situação do voto
    """
    anoatual = datetime.today().year
    idade = anoatual - ano
    if (idade < 18 and idade >= 16 ) or idade >= 65:
        return(f'Com {idade} anos: O voto é OPCIONAL!')
    elif idade < 16:
        return (f'Com {idade} anos: NÃO È PERMITIDO VOLTAR!')
    else:
        return(f'Com {idade} anos: O voto é OBRIGATORIO!')

#PROGRAMA PRINCIPAL
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
