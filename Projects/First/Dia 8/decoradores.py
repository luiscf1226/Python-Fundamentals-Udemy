def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print('adios')
    return otra_funcion

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

mayuscula_decorada=decorar_saludo(mayuscula('hola'))

'''def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def miniscula(texto):
        print(texto.lower())

    if tipo=='may':
        return mayuscula()
    if tipo=='min':
        return miniscula()


def una_funcion(funcion):
    return funcion

operacion=cambiar_letras('may')
operacion('palabra')'''


