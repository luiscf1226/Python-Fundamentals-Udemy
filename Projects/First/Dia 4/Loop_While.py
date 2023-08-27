monedas=5
while monedas >0:
    print("Tengo "+str(monedas)+" de monedas")
    monedas=monedas-1
else:
    print ("no more money gua gua ")

nombre=raw_input("your name: ")
for letra in nombre:
    if letra=='i':
        break
    print(letra)