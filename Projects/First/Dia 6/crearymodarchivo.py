archivo=open('prueba1.txt','w')
archivo.write('hola soy luis')
lista=['hola','adios','maria','mi novia']
for let in lista:
    archivo.writelines(let+'\n')
archivo.close()
archivo=open('prueba1.txt')
for ora in archivo:
    print(ora)