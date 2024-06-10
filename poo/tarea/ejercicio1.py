print('Bienvenido al programa de notas de la UNAB')

class Estudiante:
    def __init__(self, rut, nombre, edad, nota, estado, materia):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        self.estado = estado
        self.materia = materia

    def __str__(self):
        return f'Estudiante: \nRUT: {self.rut} \nNombre: {self.nombre} \nEdad: {self.edad} \nNota: {self.nota}  \nEstado: {self.estado}  \nMateria: {self.materia}'

class Notas:
    def __init__(self):
        self.Estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.Estudiantes.append(estudiante)
        print(f'Estudiante {estudiante.nombre} agregado correctamente \n')
    
    def agregar_notas(self):
        if len(self.Estudiantes) == 0:
            print('No hay estudiantes registrados, al menos registre un estudiante')
        else: 
            for i in range (len(self.Estudiantes)):
                cant_notas40 = int(input(f'Cuantas notas correspodietes al 80% seran ingresadas para {self.Estudiantes[i].nombre}: '))
                for j in range(cant_notas40):
                    print(f'Notas {80/cant_notas40}%')
                    notas40 = float(input(f'Ingrese la nota N°{j+1} de {self.Estudiantes[i].nombre}: '))
                    if notas40 >=1 and notas40 <=7:
                        self.Estudiantes[i].nota += (notas40*(0.8/cant_notas40))
                    else:
                        print('La nota no es valida, por favor ingresela de nuevo')
                        notas40 = float(input(f'Ingrese la nota N°{j+1} de {self.Estudiantes[i].nombre}: '))
                    
                cant_notas10 = int(input(f'Cuantas notas correspondiestes al 20% seran ingresadas para {self.Estudiantes[i].nombre}: '))
                for j in range(cant_notas10):
                    print(F'Notas {20/cant_notas10}%')
                    notas10 = float(input(f'Ingrese la nota N°{j+1} de {self.Estudiantes[i].nombre}: '))
                    if notas10  >= 1 and notas10 <=7:
                        self.Estudiantes[i].nota += (notas10*(0.2/cant_notas10))
                    else:
                        print('La nota no es valida, por favor ingresela de nuevo')
                        notas10 = float(input(f'Ingrese la nota N°{j+1} de {self.Estudiantes[i].nombre}: '))

inicio = True
notas = Notas()
while inicio == True:
    funcion = int(input('1.- Ingrese un Alumno. \n2.- Ingresar notas de Alumno. \n3.- Listar Notas de Alumnos. \n4.- Salir \n-> '))
    if funcion == 1:
        cant_estudiantes = int(input('Ingrese la cantidad de estudiantes: '))
        for i in range(cant_estudiantes):
            rut = input('Ingrese el RUT del estudiante: ')
            nombre = input('Ingrese el nombre del estudiante: ')
            edad = int(input('Ingrese la edad del estudiante: '))
            nota = 0
            estado = ''
            materia = input('Ingrese la materia del estudiante: ')
            estudiante = Estudiante(rut, nombre, edad, nota, estado, materia)
            notas.agregar_estudiante(estudiante)
            
    elif funcion == 2:
        notas.agregar_notas()
        for i in range(len(notas.Estudiantes)):
            if notas.Estudiantes[i].nota >= 4:
                notas.Estudiantes[i].estado = 'Aprobado'
            else:
                notas.Estudiantes[i].estado = 'Reprobado'

    elif funcion == 3:
        for i in range(len(notas.Estudiantes)):
            print(f'{notas.Estudiantes[i]}\n')
    
    elif funcion == 4:
        inicio = False
    
    else:
        print('Opcion no valida')
        