class Animal:
    def __init__(self,edad,color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print("este animal a nacido")
    def hablar(self):
        print("Este animal emite un sonido")
class Pajaro(Animal):
    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo=altura_vuelo
    def hablar(self):
        print("pio pajaro naci")
    def volar (self,metros):
        print(f"el pajaro vuela {metros} de metros")

piolin=Pajaro(3,'amarillo',34)
piolin.hablar()
piolin.volar(34)
mi_animal=Animal(23,"black")
