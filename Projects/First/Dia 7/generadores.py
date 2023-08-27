def mi_funcion():
    return 4
def mi_generador():
    x=1
    for num in range(1,1001):
        yield x
        x+=1




g=mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
