from random import choice
palabras=['panadero','animal','palabra','bye']
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def elegir_palabra(lista_palabras):
    palabra_elegida=choice(lista_palabras)
    letras_unicas=len(set(palabra_elegida))
    return palabra_elegida,letras_unicas

def pedir_letra():
    letra_elegida=''
    es_valida=False
    abecedario='abcdefghijklmnopqrstuvwxyz'
    while (es_valida==False):
        letra_elegida=raw_input("Elige una letra: ")
        if(letra_elegida in abecedario and len(letra_elegida)==1):
            es_valida=True
        else:
            print("No escogio letra correcta")
    return letra_elegida

def mostar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias
def perder():
    print("Te quedaste sin vidas")
    print("la palabra oculta era "+palabra)
    return True
def ganer(palabra_descubierta):
    mostar_nuevo_tablero(palabra_descubierta)
    print("Felicidades Ing.")

palabra,letras_unicas=elegir_palabra(palabras)
while not juego_terminado:
    print ('\n'+'*'*20+'\n')
    mostar_nuevo_tablero(palabra)
    print ('\n')
    print('Letras Incorrectas: '+'-'.join(letras_incorrectas))
    print("Vidas: "+str(intentos))
    letra=pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado




