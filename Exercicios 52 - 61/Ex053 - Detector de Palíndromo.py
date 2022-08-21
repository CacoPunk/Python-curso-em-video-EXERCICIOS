import unidecode

str = input('Digite uma frase: ').strip().upper()
str = unidecode.unidecode(str)
str = str.replace(" ", "")
str = str.replace(".", "")
str = str.replace(",", "")
reversed_string=''.join(reversed(str))
print('O inverso de {} é {}.'.format(str, reversed_string))
if str == reversed_string:
    print('Temos um Palindromo.')
else:
    print('Não temos um Palindromo')
