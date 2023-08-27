#primer manejo de archivos
mi_archivo=open('Prueba.txt')
print(mi_archivo)

print('----------')
line1=mi_archivo.readline()
#quitar salto line1.rsstrip
print(line1)
line1=mi_archivo.readline()
#quitar salto line1.rsstrip
print(line1)
mi_archivo.close()
# ejercicios de practica
mi_archivo=open('Prueba.txt')
print(mi_archivo.readlines())