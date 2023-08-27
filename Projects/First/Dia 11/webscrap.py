import bs4
import requests
#codigo para agarrar el html de la pagina
resultado = requests.get('https://www.escueladirecta.com/courses')
#convertir el texto en objeto usandp motor xml
sopa=bs4.BeautifulSoup(resultado.text,'lxml')
imagenes=sopa.select('.course-box-image')[0]['src']
imagen_curso1=requests.get(imagenes)
f=open('mi_imagen.jpg','wb')
f.write(imagen_curso1.content)
f.close()

'''imagenes=sopa.select('img')
for i in imagenes:
    if sopa.select('.course-box-image'):
        print(i)'''
'''print(imagenes)'''
'''print(sopa.select('title')[0].getText())

parrafo_especial=sopa.select('p')
print(parrafo_especial[0].getText())'''

'''columna_lateral=sopa.select('.content p')
print(columna_lateral)'''