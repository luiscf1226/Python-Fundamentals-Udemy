numeros=[1,2,3,4,5]
miv=0
for numero in numeros:
    miv+=numero
print (miv)

lista=['a','b','c']

for letra in lista:
    numero_letra=lista.index(letra)+1
    print("Letra en: " + str(numero_letra) + " es: "+letra )

lista1=['pablo','laura','fede','luis','julia']

for nombre in lista1:
    if nombre.startswith('l'):
        print (nombre)

for i in range(10):
    print("numero: "+str(i))

palabra='python'
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print (a)
    print (b)

dic={'clave1':'a','clave2':'b','clave3':'c'}
for item in dic:
    print(item)