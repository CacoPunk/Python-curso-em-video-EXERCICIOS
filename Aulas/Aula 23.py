try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/ b

except Exception as erro:
    print(f'Problema : {erro}')
except:
    print('Tivemos um erro')
else:
    print(f'O resultado é: {r:.1}')
finally:
    print('VOLTE SEMPRE')