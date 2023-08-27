class Pajaro:
    alas=True
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie
    def piar(self):
        print(f"soy el pajaro {self.especie} y hago pio")
    def volar(self,metros):
        print(f"el pajaro a volado {metros} metros WOW")
    def pintar_negro(self):
        self.color='negro'
        print(f"ahora el pajaro es {self.color}")
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} de huevos")
    @staticmethod
    def mirar():
        

Pajaro.poner_huevos(56)
piolin=Pajaro("amarillo","canario")
piolin.pintar_negro()
piolin.alas=False
print(piolin.alas)