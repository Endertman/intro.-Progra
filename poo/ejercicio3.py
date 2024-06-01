class Mamifero():
    def __init__(self, nombre):
        self.nombre = nombre

    def amamantar(self):
        print('Este animal amanta')

class Volador():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def volar(self):
        print('Este animal vuela')

class Murcielago(Mamifero, Volador):
    def __init__(self, nombre):
        Mamifero.__init__(self, nombre)
        Volador.__init__(self, nombre)

    def volar(self):
        print('Este murcielago vuela')
    
    def sonar(self):
        print('Este murcielago suena')

mi_murcielago = Murcielago('Bruce Wayne')
mi_murcielago.amamantar()
mi_murcielago.volar()
mi_murcielago.sonar()