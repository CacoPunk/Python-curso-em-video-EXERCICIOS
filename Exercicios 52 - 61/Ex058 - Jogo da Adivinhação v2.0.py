#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint
t = 1
c = randint(0, 10)
b = int(input('Tente adivinhar o numero de 0 a 10 que eu vou escolher: '))
while b != c:
    if c > b:
        b = int(input('Mais! Tente novamente: '))
        t += 1
    else:
        b = int(input('Menos! Tente novamente: '))
        t += 1
print('Parabens você acertou! Numero: {} Você precisou de {} tentativas'.format(c, t))