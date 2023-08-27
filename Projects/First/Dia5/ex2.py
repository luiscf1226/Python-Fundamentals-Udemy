def mifuncion(palabra):
    mi_set=set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista=list(mi_set)
    mi_lista.sort()
    return mi_lista
pal=mifuncion("entretenido")
print(pal)
print(range(1,10))