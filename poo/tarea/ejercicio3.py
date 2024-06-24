import pandas as pd
print('Bienvenido al Gran Hotel Santiago')
huespedes = []
class Huesped:
    def __init__(self, nombre, nacionalidad, tipo_documento, numero_documento, dias_hospedado):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.dias_hospedado = dias_hospedado

class Registro(Huesped):
    def __init__(self, nombre, nacionalidad, tipo_documento, numero_documento, dias_hospedado):
        super().__init__(nombre, nacionalidad, tipo_documento, numero_documento, dias_hospedado)

    def registrar(self):
        num_huepedes = int(input('Ingrese la cantidad de huespedes: '))
        for i in range(num_huepedes):
            nombre = (input('Ingrese nombre: '))
            nacionalidad = (input('Ingrese nacionalidad: '))
            tipo_documento = (input('Tipo de documento: '))
            numero_documento = int((input('Numero de documento: ')))
            dias_hospedado = int((input('Ingrese dias hospedado: ')))

            huesped = Huesped(nombre, nacionalidad, tipo_documento, numero_documento, dias_hospedado)
            huespedes.append(huesped)

class Consumo:
    def __init__(self,nombre_servicio,precio_servicio):
        self.nombre_servicio = nombre_servicio
        self.precio_servicio = precio_servicio

# Servicios
plato1 = Consumo('Pizza Familiar', 20000)
plato2 = Consumo('Filete con papas bravas', 23000)
plato3 = Consumo('Ceviche', 8000)
plato4 = Consumo('Merluza Frita con Acompañamiento', 14000) 
bar1 = Consumo('Pisco + Bebida', 14000) 
bar2 = Consumo('Whisky Jonny Walker + Bebida', 30000) 
bar3 = Consumo('Cervezas Quilmes Pack 6', 7000) 
bar4 = Consumo('Bebidas 1.5 Litros', 2500)

class Compras(Consumo):
    def __init__(self, nombre_servicio, precio_servicio):
        super().__init__(nombre_servicio, precio_servicio)

    def agregar_compras(self):

        consumo_huespedes = []
        if len(huespedes) == 0:
            print('Registre Huespedes')
        
        else:
            for huesped in huespedes:
                print(f'{huesped+1}. {Huesped.nombre}')
        huesped_elegido = int(input('Seleccione un huesped: '))
        iniciador_servicios = True
        while iniciador_servicios == True:
            seleccion_tipo_servicio =  int(input('-1 Comida \n 2- Bebidas'))
            if seleccion_tipo_servicio == 1:
                seleccion_comida = int(input('Seleccione el servicio: \n -1 Pizza Familiar \n 2- Filete con papas bravas \n 3- Ceviche \n 4- Merluza Frita con Acompañamiento'))        
                if seleccion_comida == 1:
                    fecha_consumo = input('Ingrese la fecha de consumo: ')
                    hora__consumo = int(input('Ingrese la hora de consumo (24hrs): '))
                    
                    

            
            




    
