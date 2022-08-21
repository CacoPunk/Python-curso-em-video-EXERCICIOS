def string_to_int(s):
    try:
        temp = int(s)
        if type(temp) == int:
            return temp
    except:
        return(0)


val = string_to_int('a')
print(val)