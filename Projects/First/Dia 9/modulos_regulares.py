import re
texto='Si necesitas ayuda llama al (658)-598-7567 las 24 horas al servicio de ayuda online'

patron='ayuda'
busqueda=re.findall(patron,texto)

print(busqueda)

texto2="llama al 564-545-3453 ya mismo"
patron=r'\d\d\d-\d\d\d-\d\d\d\d'
patron2=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado=re.search(patron2,texto2)
print(resultado.group())

clave=input('Clave: ')
patron3=r'\D{1}\w{7}'
cheq=re.search(patron3,clave)
print(cheq)

texto3="No atendemos los miercoles por la tarde"
buscar=re.search(r'lunes|martes',texto3)
print(buscar)