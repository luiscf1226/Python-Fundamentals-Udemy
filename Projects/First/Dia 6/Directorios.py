import os
ruta=os.getcwd()
print(ruta)
#os.chdir() para cambiar ruta
#ruta=os.makedirs('D:\luis flores unitec\luis flores unitec\Cursos\PYTHON\Projects\First\Dia 6\otra') para crear dirs
ruta2='D:\luis flores unitec\luis flores unitec\Cursos\PYTHON\Projects\First\Dia 6'
elemento=os.path.basename(ruta2)
print(elemento)
elemento=os.path.dirname(ruta2)
print(elemento)
#os.rmdir para eliminar
arch=open('C:\\ruta\\arch2.txt')
print(arch.read())