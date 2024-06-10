class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bread(self):
        print('This animal bread')

class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race
    
    def ladrar(self):
        print('This dog ladra')

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def maullar(self):
        print('This cat maulla')

my_dog = Dog('Bruno', 3, 'Labrador')

my_dog.bread()
my_dog.ladrar()

my_cat = Cat('Mimi', 2, 'Blanco')

my_cat.bread
my_cat.maullar

for i in range (len(self.Estudiantes)):
    cant_notas40 = 2 #int(input(f'Cuantas notas de 40% seran ingresadas para {self.Estudiantes[i].nombre}: '))
    for j in range(cant_notas40):
        print('Notas 40%')
        notas40 = float(input(f'Ingrese la nota N°{j+1} de {self.Estudiantes[i].nombre}: '))
        self.Estudiantes[i].nota += (notas40*(0.4))/cant_notas40
        
    cant_notas10 = 2 #int(input(f'Cuantas notas de 10% seran ingresadas para {self.Estudiantes[i].nombre}: '))
    for j in range(cant_notas10):
        print('Notas 10%')
        notas10 = float(input(f'Ingrese la nota N°{j+1} de {self.Estudiantes[i].nombre}: '))
        self.Estudiantes[i].nota += (notas10*0.1)/cant_notas10 
