def devolver_distintos(n1,n2,n3):
    suma=n1+n2+n3
    lista=[n1,n2,n3]
    if suma>15:
        return max(lista)
    elif suma<10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

num=devolver_distintos(3,1,5)
print(num)