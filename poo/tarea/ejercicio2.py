import uuid #Modulo/Libreria para generar codigos unicos
print('Aplicación Envios Instantaneos')

class Repartidor: #Inicio clase con el constructor __init__ aqui definire los rasgos o caracterizticas esenciales del repartidor         
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    def __str__(self): #Con el metodo __str__ le especifico la forma de imprimir la clase cuando la llame (ej. print(Repartidor)) de no hacerlo asi me mostraria la direccion en la memoria ram y no los datos
        return f'Repartidor: \nRUT: {self.rut} \nNombre: {self.nombre}'
class Envio: #Inicio clase con el constructor __init__ con las caractirizticas del paquete
    def __init__(self, codigo, peso, precio, estado):
        self.codigo = codigo
        self.peso = peso
        self.precio = precio
        self.estado = estado

    def __str__(self): #Misma logica al usar __str__
        return f'Envio: \nPeso: {self.peso} \nCodigo: {self.codigo}'
class Clientes: #Inicio clase padre clientes, esta clase tendra las caracterizticas del cliente las cuales herederan los remitentes y receptores
    def __init__(self, rut, nombre, direccion, comuna, region, pais):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.comuna = comuna
        self.region = region
        self.pais = pais
class Remitente(Clientes): #Clase hija de Clientes
    def __init__(self,rut,nombre,direccion,comuna,region,pais): #Inicio la clase con el constructor
        super().__init__(rut, nombre, direccion, comuna, region, pais) #Heredo de la clase padre con el metodo __super__

    def __str__(self): #misma logica para imprimir
        return f'Remitente: \nRUT: {self.rut} \nNombre: {self.nombre} \nDireccion: {self.direccion} \nComuna: {self.comuna} \nRegion: {self.region}'
 
class Receptor(Clientes): #Misma logica que remitente
    def __init__(self, rut, nombre, direccion, comuna, region, pais):
        super().__init__(rut, nombre, direccion, comuna, region, pais)

    def __str__(self): #misma logica para imprimir
        return f'Remitente: \nRUT: {self.rut} \nNombre: {self.nombre} \nDireccion: {self.direccion} \nComuna: {self.comuna} \nRegion: {self.region}'
class Envios: #Genero la clase Envios, donde tendre toda la logica de los repatidores y los envios
    def __init__(self):
        self.Repartidores = []
        self.Envios = []
    
    def agregar_repartidor(self, repartidor): #esta funcion luego de que el usuario genere los repartidores los guardara en una lista
        self.Repartidores.append(repartidor)
        print(f'Repartidor {repartidor.nombre} agregado correctamente \n')
    
    def agregar_envio(self): #Esta funcion recorre la lista creada anteriormente donde estan los repartidores para agregarle un envio a el mismo
        for i in range(len(self.Repartidores)): #Entonces recorre la lista e imprimira cada repartidor
            print(f'{i+1}. {self.Repartidores[i]}')
        repartidor_seleccionado = int(input('Seleccione un repartidor: ')) #Se pide que se seleccione un repartidor
        print(f'Repartidor {self.Repartidores[repartidor_seleccionado-1].nombre} seleccionado')
        cant_envios = int(input(f'Ingrese la cantidad de envios a registrar para {self.Repartidores[repartidor_seleccionado-1].nombre}: '))
        for i in range(cant_envios):
            info_envio = []

            codigo = str(uuid.uuid4())
            peso = float(input('Ingrese el peso del envio: '))
            if peso <= 1:
                precio = 1800
            elif peso > 1 and peso < 10:
                precio = 1800 + (peso-1)*1000
            elif peso > 10:
                for kilo in range(0,((peso-10)):
                    if kilo % 10 == 0 and kilo < 100:

                        
                

                    

                        
            
            estado = 'Asignado'
            paquete = Envio(codigo, peso, precio, estado)
            info_envio.append(paquete)

            rut_remitente = input('Ingrese el RUT del remitente: ')
            remitente = input('Ingrese el nombre del remitente: ')
            direccion_remintente = input('Ingrese la direccion del remitente: ')
            comuna_remintente = input('Ingrese la comuna del remitente: ')
            region_remintente = input('Ingrese la region del remitente: ')
            pais_remintente = input('Ingrese el pais del remitente: ')
            remitente = Remitente(rut_remitente, remitente, direccion_remintente, comuna_remintente, region_remintente, pais_remintente)
            info_envio.append(remitente)

            rut_receptor = input('Ingrese el RUT del receptor: ')
            receptor = input('Ingrese el nombre del receptor: ')
            direccion_receptor = input('Ingrese la direccion del receptor: ')
            comuna_receptor = input('Ingrese la comuna del receptor: ')
            region_receptor = input('Ingrese la region del receptor: ')
            pais_receptor = input('Ingrese el pais del receptor: ')
            receptor = Receptor(rut_receptor, receptor, direccion_receptor, comuna_receptor, region_receptor, pais_receptor)
            info_envio.append(receptor)

            self.Envios.append((self.Repartidores[repartidor_seleccionado-1], info_envio))
        
    def modificar_envio(self):
        for i in range(len(self.Envios)):
            print(f'Envio N{i+1}° \n{self.Envios[i][0]}\n')
            for j in range(len(self.Envios[i][1])):
                print(f'\n{self.Envios[i][1][j]}\n\n\n')
        envio_seleccionado = int(input('Seleccione un envio: '))
        print(f'Envio N{envio_seleccionado} seleccionado')
        print('1.- Modificar Estado\n 2. Volver al menú\n')
        
        

inicio = True
envios = Envios()
while inicio == True:
    funcion = int(input('1.- Ingrese un repartidor. \n2.- Ingrese un envio. \n3.- Modifique un envio. \n4.- Listar todos los envios \n5.- Salir \n-> '))
    if funcion == 1:
        cant_repartidores = int(input('Ingrese la cantidad de repartidores: '))
        for i in range(cant_repartidores):
            rut = input('Ingrese el RUT del repartidor: ')
            nombre = input('Ingrese el nombre del repartidor: ')
            repartidor = Repartidor(rut, nombre)
            envios.agregar_repartidor(repartidor)
            
    elif funcion == 2:
        if len(envios.Repartidores) == 0:
            print('No hay Repartidores registrados, por favor registre al menos uno')
        else:
            print('Seleccione un repartidor para realizar el envío')
            envios.agregar_envio()

    elif funcion == 3:
        if len(envios.Envios) == 0:
            print('No hay envios registrados')
        else:
            print('Modificar envio')
            envios.modificar_envio()

    elif funcion == 4:
        print('listando')
    
    elif funcion == 5:
        inicio = False
    
    else:
        print('Opcion no valida')    
    
        