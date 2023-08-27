class Padre:
    def hablar(self):
        print("hola de padre")
class Madre:
    def reir(self):
        print("jaja mami")
    def hablar(self):
        print("qtal")
class Hijo(Padre,Madre):
    pass
class Nieto(Hijo):
    pass

mi_nieto=Nieto()
mi_nieto.hablar()
mi_nieto.reir()

