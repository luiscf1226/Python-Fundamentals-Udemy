def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado=chequear_3_cifras(434)
print (resultado)
def chequear_cifras(lista):
    listac=[]
    for n in lista:
        if n in range(100,1000):
             listac.append(n)
        else:
            pass
    return listac
resul=chequear_cifras([535,66,448])
print(resul)