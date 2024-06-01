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