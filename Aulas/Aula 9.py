frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:13:2])
print(frase[::2])
print(frase.count('o'))
print(len(frase))
frase.replace('Python', 'Android')
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
a = frase.split()
print(a)
print(a[0])


print("""RagnaTales é um servidor Pré-Renovação, Low Rate e que trás diversas novas configurações e
sistemas, o transformando em um servidor único!
Contanto com a mesma equipe do projeto ragnaWave, já provamos que nossa equipe é extremamente 
capacitada para trazer aos brasileiros o melhor do Ragnarok Online!

Seriedade, profissionalismo e educação para com os jogadores é o mínimo que o podemos oferecer.
Planejamento, inovação e criatividade é o que adicionamos nessa equação para alcançar um resultado que
agrade todos os tipos de jogadores, desde os nostálgicos casuais até os mais dedicados e dispostos a 
serem os melhores de Rune- Midgard!""")
