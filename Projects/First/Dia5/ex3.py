def ceros_vecinos(*args):
    contador=0
    for num in args:
        if args[contador]==0 and args[contador+1]==0:
            return True
        else:
            contador+=1
    return False
print(ceros_vecinos(0,2,23,2,23,0,0))