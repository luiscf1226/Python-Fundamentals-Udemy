def suma(**kwargs):
    for clavew,valor in kwargs.items():
        print(clavew+" es igual a: "+str(valor))

suma(x=3,y=5,z=2)