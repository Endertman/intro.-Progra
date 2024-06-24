#Formas de escribir en Python
nombre_apellido = 'Snake Case' #Para variables y funciones siempre usamos este
nombreApellido = 'CamelCase'
NombreApellido = 'PascalCase' #Para clases siempre usaremos este

#Creando una función

def receta():
    pass #Es una forma de que el codigo no se detenga por una funcion o metodo vacio

#Creando una clase

class RecetaGalletas:
    def __init__(self, harina, huevos, azucar, aceite):
        self.harina = harina
        self.huevos = huevos
        self.azucar = azucar
        self.aceite = aceite
        self.sal = '1 pizca'
    
    def __str__(self):
        return f'la galleta lleva {galleta1.harina} de harina, lleva {galleta1.huevos}, tambien lleva {galleta1.azucar} de azucar, {galleta1.aceite} y {galleta1.sal} sal'

    def galleta(self):
        print(f'Galleta lista, {galleta1}')

galleta1 = RecetaGalletas('500 gr', '2 huevos', '2 kg', '200 ml')
galleta1.galleta()

#Herencia
class Persona:
    def __init__(self,nombre,edad,respirar):
        self.nombre = nombre
        self.edad = edad
        self.respirar = respirar
    
class Cantante(Persona):
    def __init__(self,nombre,edad,respirar,estilo,popularidad):
        super().__init__(nombre,edad,respirar)
        self.estilo = estilo
        self.popularidad = popularidad

class Estudiante(Persona):
    def __init__(self, nombre, edad, respirar, promedio, curso):
        super().__init__(nombre, edad, respirar)
        self.promedio = promedio
        self.curso = curso
     
juanito = Persona('Juanito',18,False)
matias = Cantante('Matias', 18, True, 'Bachata', 'Media')
isabella = Estudiante('Isabella', 19, True, 6.8, 'Programacion')

#Herencia doble
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def respirar(self):
        print('El animal respira')

class Mamifero(Animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)

    def amamantar(self):
        print('Amamantar')
    
class Volador(Animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
        
        
    def volar(self):
        print('Esta volao')

class Noctulo(Mamifero,Volador):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)

class Vaca(Mamifero):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)

pepe = Noctulo('Murcielago', 8)
lola = Vaca('Vaca', 8)

pepe.amamantar()
pepe.respirar()
pepe.volar()

lola.amamantar()


        








