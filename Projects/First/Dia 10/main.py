import pygame
import math
import random
from pygame import mixer
pygame.init()
#definir la pantalla del juego alto y ancho
pantalla=pygame.display.set_mode((800,600))
#Titulo e Icono
pygame.display.set_caption("Space Game Luis Flores")
icono=pygame.image.load("galxy.png")
pygame.display.set_icon(icono)
fondo=pygame.image.load('Fondo.jpg')

se_ejecuta=True
#Jugador principal

img_jugador=pygame.image.load('rocket.png')
#variables jugador
jugador_x=368
jugador_y=500
jugador_x_cambio=0
#variables enemigo
img_enemigo= []
enemigo_x=[]
enemigo_y=[]
enemigo_x_cambio=[]
enemigo_y_cambio=[]
cantidad_enemigos=8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)
#variables bala
img_bala=pygame.image.load('bala.png')
bala_x=0
bala_y=500
bala_x_cambio=0
bala_y_cambio=0.9

bala_visible=False
#puntaje
puntaje=0
fuente=pygame.font.Font('blazed.ttf',22)
texto_x=10
texto_y=10
#texto final
fuente_final=pygame.font.Font('blazed.ttf',40)
def texto_final():
    mi_fuente_final=fuente_final.render("ELIMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))
#musica
'''mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)'''
#funcion puntuaje
def mostrar_puntuaje(x,y):
    texto=fuente.render(f'PUNTAJE: {puntaje}',True,(255,255,255))
    pantalla.blit(texto,(x,y))
#funcion enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))
#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible=True
    pantalla.blit(img_bala,(x+16,y+10))
#detectar colision
def hay_colision(x_1,y_1,x_2,y_2):

    distancia=math.sqrt(math.pow(x_1-x_2,2)+math.pow(y_2-y_1,2))
    if distancia<27:
        return True
    else:
        False
#loop del juego
while se_ejecuta:
    # ver si se cancela
    # llenando la pantalla con un color usando formato rgb
    pantalla.blit(fondo,(0,0))
    #iterar evento
    for evento in pygame.event.get():
        #evento que cancela la pantalla con la x
        if evento.type==pygame.QUIT:
            se_ejecuta=False
        #evento presionar teclas
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_LEFT:
                jugador_x_cambio=-0.6

            if evento.key==pygame.K_RIGHT:
                jugador_x_cambio = 0.6

            if evento.key==pygame.K_SPACE:
                sonido_bala=mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if bala_visible==False:
                    bala_x=jugador_x
                    disparar_bala(bala_x,bala_y)

        #evento soltar
        if evento.type==pygame.KEYUP:
            if evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT:
               jugador_x_cambio=0
    #modificar ubicacion
    jugador_x+=jugador_x_cambio
    #posicion enemigo
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[e]>500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000
            texto_final()
            break
        enemigo_x[e]+=enemigo_x_cambio[e]
        if (enemigo_x[e] <= 0):
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e]=random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e],e)

    #matener dentro del borde
    if(jugador_x<=0):
        jugador_x=0
    if jugador_x>=736:
        jugador_x=736



    #movimientos
    if bala_y<=-64:
        bala_y=500
        bala_visible=False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambio




    jugador(jugador_x,jugador_y)
    mostrar_puntuaje(texto_x,texto_y)
    #actualizar
    pygame.display.update()

