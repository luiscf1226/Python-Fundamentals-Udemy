import re
import os
import time
import datetime
from pathlib import Path
import math

ruta='D:\\luis flores unitec\\luis flores unitec\\Cursos\\PYTHON\\Projects\\First\\Dia 9\\proyecto\\Mi_Gran_Directorio'
mi_patron=r'N\D{3}-\d{5}'
hoy=datetime.date.today()
nros_encontrados=[]
arrchivos_encontrados=[]

def buscar_numero(archivo,patron):
    este_archivo=open(archivo,'r')
    texto=este_archivo.read()
