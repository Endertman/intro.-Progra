print('Aplicación Envios Instantaneos')

class Repartidor:
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    def __str__(self):
        return f'Repartidor: \nRUT: {self.rut} \nNombre: {self.nombre}'

class Envios:
    def __init__(self):
        self.Repartidores = []
        self.Envios = []
    
    def agregar_repartidor(self, repartidor):
        self.Repartidores.append(repartidor)
        print(f'Repartidor {repartidor.nombre} agregado correctamente \n')
    
    def seleccionar_repartidor(self):
        if len(self.Repartidores) == 0:
            print('No hay Repartidores registrados, por favor registre al menos uno')
        else: 
            for i in range(len(self.Repartidores)):
                print(f'{i+1}. {self.Repartidores[i]}')
            repartidor_seleccionado = int(input('Seleccione un repartidor: '))
            print(f'Repartidor {self.Repartidores[repartidor_seleccionado-1].nombre} seleccionado')
      
    def agregar_envio(self):

        cant_envios
        

inicio = True
envios = Envios()
while inicio == True:
    funcion = int(input('1.- Ingrese un repartidor. \n2.- Ingrese un envio. \n3.- Modifique un envio. \n4. -Listar todos los envios \n5.- Salir \n-> '))
    if funcion == 1:
        cant_repartidores = int(input('Ingrese la cantidad de repartidores: '))
        for i in range(cant_repartidores):
            rut = input('Ingrese el RUT del repartidor: ')
            nombre = input('Ingrese el nombre del repartidor: ')
            repartidor = Repartidor(rut, nombre)
            envios.agregar_repartidor(repartidor)
            
    elif funcion == 2:
        print('Seleccione un repartidor para realizar el envío')
        envios.seleccionar_repartidor()




    elif funcion == 3:
        print('Modificar envio')

    elif funcion == 4:
        print('listando')
    
    elif funcion == 5:
        inicio = False
    
    else:
        print('Opcion no valida')    
    
        