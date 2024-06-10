class Student:
    def __init__(self, rut, name, age, subjet,):
        self.rut = rut
        self.name = name
        self.age = age
        self.subjet = subjet

    def __str__(self):
        return f'{self.name} is {self.age} years old and studies {self.subjet}'

class Average(Student):
    def __init__(self, rut, name, age, subjet):
        super().__init__(rut, name, age, subjet)

number_students = int(input("Ingrese el numero de estudiantes: "))

students = []

for i in range(number_students):
    rut = input("Ingrese el rut del estudiante: ")
    name = input("Ingrese el nombre del estudiante: ")
    age = int(input("Ingrese la edad del estudiante: "))
    subject = input("Ingrese la materia del estudiante: ")
    student = (rut, name, age, subject)
    students.append(student)

def student():
    for i in range (len(students)):
        return Student(students[i])

    