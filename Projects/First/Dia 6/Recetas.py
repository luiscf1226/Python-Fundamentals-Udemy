import os
from pathlib import Path
from os import system
#Menu Inicial
mi_ruta=Path(Path.home(),"Recetas")
def contar_recetas(ruta):
    cont=0
    for arch in Path(ruta).glob("**/*.txt"):
        cont+=1
    return cont

def inicio():
    system('cls')
    print("*"*50)
    print("Bienvenido al administrador de Recetas")
    print("*" * 50)
    print('\n')
    print(f"Las recetas estan en {mi_ruta} y tiene un total de recetas de: {contar_recetas(mi_ruta)}")
inicio()
menu=0
if menu==1:
    #mostrar categorias
    #elegir categoria
    #mostrar recetas
    #elegir recetas
    #leer la receta
    #volver inico
    pass
elif menu==2:
    #mostrar categorias
    #elegir categoria
    #crear receta y volver
    pass
elif menu==3:
    #crear categoria
    #volver inicio
    pass
elif menu==4:
    # mostrar categorias
    # elegir categoria
    # mostrar recetas
    # elegir recetas
    # eliminar  la receta
    # volver inico
    pass
elif menu==5:
    # mostrar categorias
    # elegir categoria
    #liminar categoria
    #volver
    pass
elif menu==6:
    #finalizar
    pass