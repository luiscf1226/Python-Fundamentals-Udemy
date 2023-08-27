class Animal:
    def __init__(self,edad,color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print("este animal a nacido")
    pass
class Pajaro(Animal):
    pass
piolin=Pajaro(2,'amarillo')
piolin.nacer()
print(piolin.color,piolin.edad)