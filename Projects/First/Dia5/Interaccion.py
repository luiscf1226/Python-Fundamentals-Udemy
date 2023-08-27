from random import *
#lista inicial
palitos=['-','--','---','----']
#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento=raw_input("Elige numero 1-4 : ")
    return int(intento)

#comprobaar
def chequear_intento(lista,intento):
    if lista[intento-1]=='-':
        print("tenes la mas pequeniaa")
    else:
        print("pison")
    print("Te toco el palito:  "+lista[intento-1])

palitos_mezclados=mezclar(palitos)
selecction=probar_suerte()
chequear_intento(palitos_mezclados,selecction)
