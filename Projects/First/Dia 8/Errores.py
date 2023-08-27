def pedir():
    while True:
        try:
            numero=int(input("ingrese numero: "))
        except:
            print("no es numero")
        else:
            print("ingresaste el numero : "+str(numero))
            break



pedir()
'''def suma():
    n1=int(input("numero 1: "))
    n2 =int(input("numero 2: "))
    print(f"resultado: {n1+n2}")
    print("gracias por sumar: "+0)


try:
    suma()
except TypeError:
    print("estas intentando tipos distintos")
except ValueError:
    print("ese no es un numero")
else:
    print("si se pudo sumar.....")
finally:
    print("eso fue todo")'''