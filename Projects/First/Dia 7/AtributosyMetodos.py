class Pajaro:
    alas=True
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie
    def piar(self):
        print(f"soy el pajaro {self.especie} y hago pio")
    def volar(self,metros):
        print(f"el pajaro a volado {metros} metros WOW")
mi_pajaro=Pajaro('azul','tucan')
print(mi_pajaro.color,mi_pajaro.especie,mi_pajaro.alas)
mi_pajaro.piar()
mi_pajaro.volar(50)