#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(*nt, sit=False):
    """
    Digite quantas notas precisar para analisar total, maior nota , menor nota, média e sitação(opcional)
    :param nt: notas
    :param sit: True(para mostrar)
    :return: dicionario com as informações.
    """
    x = dict()
    m = 0
    x['total'] = len(nt)
    x['maior'] = max(nt)
    x['menor'] = min(nt)
    x['média'] = sum(nt)/len(nt)
    if sit:
        if x['média'] < 5:
            x['sitação'] = 'RUIM'
        elif x['média'] > 7:
            x['sitação'] = 'RAZOÁVEL'
        else:
            x['sitação'] = 'BOA'
    return(x)

#PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)