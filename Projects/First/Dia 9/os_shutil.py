import os
import shutil
import send2trash
'''print(os.getcwd())
archivo=open('curso.txt','w')
archivo.write('ojala funcione')
archivo.close()
'''
#shutil.move('curso.txt','D:\\luis flores unitec')
#send2trash.send2trash('curso.txt')
#print(os.walk())
ruta='D:\\luis flores unitec\\mm'
for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f'en la carpeta: {ruta}')
    print(f'las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')
