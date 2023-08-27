import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
id1='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

#escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #almacenar el reconocedor
    r=sr.Recognizer()
    #configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold=0.8
        #informar que comenzo a grabar
        print("ya puede hablar")

        #guardar el audio
        audio=r.listen(origen)
        try:
            #buscar en google
            pedido=r.recognize_google(audio,language="es-mx")
            #prueba de que se puido
            print("dijiste: "+str(pedido))
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print("ups no entendi")
            #devolver
            return "sigo esperando"
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("ups no hay servicio")
            # devolver
            return "sigo esperando"
        except:
            # prueba de que no comprendio el audio
            print("ups algo salio mal")
            # devolver
            return "sigo esperando"
    return pedido
#funcion para que el asistente hable
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine=pyttsx3.init()
    engine.setProperty('voice',id1)
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
#transformar_audio_en_texto()
#hablar("Hola Mundo soy el hijo de puta de denis ")
#informar dia
def pedir_dia():
    #crear la variable con datos de hoy
    dia=datetime.date.today()

    #crear variable dia semana
    dia_semana=dia.weekday()

    #diccionario con nombres de los dias
    calendario={0:'Lunes',
                1:'Martes',
                2:'Miercoles',
                3:'Jueves',
                4:'Viernes',
                5:'Sabado',
                6:'Domingo'}
    #decir el dia

    hablar(f'El Dia de hoy es: {calendario[dia_semana]}. La Fecha es: {dia}')
#informar que hora es
def pedir_hora():
    #crear variable con datos de la hora
    hora=datetime.datetime.now()
    hora=f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos.  '
    print(hora)
    #decir la hora
    hablar(hora)
#saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora=datetime.datetime.now()
    if hora.hour<6 or hora.hour>20:
        momento='Buenas Noches'
    elif 6 <= hora.hour < 13:
        momento='Buen Dia'
    #saludar
    else:
        momento='Buenas Tardes'
    hablar(f'{momento}, soy Helena, tu ayuda automatizada. Como te Puedo Ayudar?')
#funcion central
def pedir_cosas():
    #activar saludo
    saludo_inicial()
    #variable de corte
    comenzar=True
    while comenzar:
        #activar el micro y guardar el pedido de string
        pedido=transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con Gusto. Ahorita Estoy Abriendo Youtube para ti')
            webbrowser.open('https://www.youtube.com')
        elif 'abrir navegador' in pedido:
            hablar('Con Gusto. Ahorita Estoy Abriendo Navegador para ti')
            webbrowser.open('https://www.google.com')
        elif 'día es hoy'in pedido:
            pedir_dia()
            continue
        elif 'hora es' in pedido:
            pedir_hora()
            continue
pedir_cosas()

