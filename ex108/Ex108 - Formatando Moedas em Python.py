#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
# como um valor monetário formatado.
#108 e 109, 110, 111, 112
from ex108.utilidadesCeV import moeda as md
from ex108.utilidadesCeV import dado

num = dado.leiaDinheiro('Digite o valor: R$')
#print(f'A metade de {md.moeda(num)} é {md.metade(num)}')
#print(f'O dobro de {md.moeda(num)} é {md.dobro(num)}')
#print(f'aumentando 10%, temos {md.aumentar(num, 10)}')
#print(f'Diminuindo 15%, temos {md.diminuir(num, 15)}')
md.resumo(num, 10, 20)