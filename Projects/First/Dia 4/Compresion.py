palabra='python'
lista=[]
for letra in palabra:
    lista.append(letra)
print(lista)
palabra='python Es Mejor'
lista2=[letra for letra in palabra]
print(lista2)
lista3=[n for n in range(0,21,2)if n*2 >10]
print(lista3)
lista3=[n*2 for n in range(0,21,2)]
print(lista3)