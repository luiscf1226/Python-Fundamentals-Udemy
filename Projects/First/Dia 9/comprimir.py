import zipfile
import shutil
'''carpeta_origen='D:\\luis flores unitec\\mm'
archivo_destino='Todo_Comprimido'
shutil.make_archive(archivo_destino,'zip',carpeta_origen)'''
shutil.unpack_archive('Todo_Comprimido','Extraccion Terminada','zip')

#usando zipfile
'''zip_abierto=zipfile.ZipFile('archivo_comprimido.zip','r')
zip_abierto.extractall()'''

'''mi_zip=zipfile.ZipFile('archivo_comprimido.zip','w')
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')
mi_zip.close()'''