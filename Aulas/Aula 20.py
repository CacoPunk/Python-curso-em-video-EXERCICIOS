def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1

valores= [1, 2, 3]
dobrar(valores)
print(valores)