import time
import timeit
'''def prueba_for(numero):
    lista=[]
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista=[]
    contador=1
    while contador <=numero:
        lista.append(contador)
        contador+=1
    return lista
'''
declaracion='''
prueba_for(10)
'''
mi_setup='''
lista=[]
    for num in range(1,numero+1):
        lista.append(num)
    return lista
'''
durar=timeit.timeit(declaracion,mi_setup,number=1000)
print(durar)
'''inicio=time.time()
prueba_for(133333)
final=time.time()
print(final-inicio)

inicio=time.time()
prueba_while(333333)
final=time.time()
print(final-inicio)'''