nombre=raw_input("Cual es tu Nombre: ")
from random import *
intentos=8
num=randint(1,100)
while(intentos>0):
    print("Bienvenido al Juego: "+nombre)

    adivina=int(raw_input("Adivina el numero: "))
    if adivina>100 and adivina<1:
        print("Numero Invalido Perdiste Turno")
        intentos -= 1
        print("Intentos Restantes: " + str(intentos))
    elif adivina<num:
        print("Numero Menor")
        intentos -= 1
        print("Intentos Restantes: " + str(intentos))
    elif adivina>num:
        print("Numero  Mayor")
        intentos -= 1
        print("Intentos Restantes: " + str(intentos))
    elif adivina==num:
        print("Ganaste")
        intentos=0
        break

