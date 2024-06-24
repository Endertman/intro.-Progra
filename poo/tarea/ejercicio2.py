import uuid # Módulo para generar códigos únicos

print('Aplicación Envios Instantaneos')

class Repartidor:         
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    def __str__(self):
        return f'Repartidor: \nRUT: {self.rut} \nNombre: {self.nombre}'

class Envio:
    def __init__(self, codigo, peso, precio, estado):
        self.codigo = codigo
        self.peso = peso
        self.precio = precio
        self.estado = estado

    def __str__(self):
        return f'Envio: \nPeso: {self.peso} \nCodigo: {self.codigo} \nPrecio: {self.precio:.2f} \nEstado: {self.estado}'

class Clientes:
    def __init__(self, rut, nombre, direccion, comuna, region, pais):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.comuna = comuna
        self.region = region
        self.pais = pais

class Remitente(Clientes):
    def __init__(self, rut, nombre, direccion, comuna, region, pais):
        super().__init__(rut, nombre, direccion, comuna, region, pais)

    def __str__(self):
        return f'Remitente: \nRUT: {self.rut} \nNombre: {self.nombre} \nDireccion: {self.direccion} \nComuna: {self.comuna} \nRegion: {self.region}'

class Receptor(Clientes):
    def __init__(self, rut, nombre, direccion, comuna, region, pais):
        super().__init__(rut, nombre, direccion, comuna, region, pais)

    def __str__(self):
        return f'Receptor: \nRUT: {self.rut} \nNombre: {self.nombre} \nDireccion: {self.direccion} \nComuna: {self.comuna} \nRegion: {self.region}'

class Envios:
    def __init__(self):
        self.Repartidores = []
        self.Envios = []
    
    def agregar_repartidor(self, repartidor):
        self.Repartidores.append(repartidor)
        print(f'Repartidor {repartidor.nombre} agregado correctamente \n')
    
    def calcular_precio_envio(self, peso):
        precio_base = 1800
        costo_por_kilo = 1000
        descuento = 0.05
        max_descuento_kilos = 100

        if peso <= 1:
            return precio_base
        elif peso > 1 and peso < 10:
            return precio_base + (peso - 1) * costo_por_kilo
        else:
            precio = precio_base + 9 * costo_por_kilo  # Costo hasta 10 kilos
            peso_extra = peso - 10
            while peso_extra > 0:
                kilos_a_cobrar = min(10, peso_extra)
                descuento_aplicado = min((peso - 10) // 10, 10)  # Descuento aplicado en bloques de 10 kilos
                costo_por_kilo_con_descuento = costo_por_kilo * (1 - descuento * descuento_aplicado)
                precio += kilos_a_cobrar * costo_por_kilo_con_descuento
                peso_extra -= kilos_a_cobrar
            return precio

    def agregar_envio(self):
        for i in range(len(self.Repartidores)):
            print(f'{i+1}. {self.Repartidores[i]}')
        repartidor_seleccionado = int(input('Seleccione un repartidor: '))
        print(f'Repartidor {self.Repartidores[repartidor_seleccionado-1].nombre} seleccionado')
        cant_envios = int(input(f'Ingrese la cantidad de envios a registrar para {self.Repartidores[repartidor_seleccionado-1].nombre}: '))
        for i in range(cant_envios):
            info_envio = []

            codigo = str(uuid.uuid4())
            peso = float(input('Ingrese el peso del envio: '))
            precio = self.calcular_precio_envio(peso)
            
            estado = 'Asignado'
            paquete = Envio(codigo, peso, precio, estado)
            info_envio.append(paquete)

            rut_remitente = input('Ingrese el RUT del remitente: ')
            nombre_remitente = input('Ingrese el nombre del remitente: ')
            direccion_remitente = input('Ingrese la direccion del remitente: ')
            comuna_remitente = input('Ingrese la comuna del remitente: ')
            region_remitente = input('Ingrese la region del remitente: ')
            pais_remitente = input('Ingrese el pais del remitente: ')
            remitente = Remitente(rut_remitente, nombre_remitente, direccion_remitente, comuna_remitente, region_remitente, pais_remitente)
            info_envio.append(remitente)

            rut_receptor = input('Ingrese el RUT del receptor: ')
            nombre_receptor = input('Ingrese el nombre del receptor: ')
            direccion_receptor = input('Ingrese la direccion del receptor: ')
            comuna_receptor = input('Ingrese la comuna del receptor: ')
            region_receptor = input('Ingrese la region del receptor: ')
            pais_receptor = input('Ingrese el pais del receptor: ')
            receptor = Receptor(rut_receptor, nombre_receptor, direccion_receptor, comuna_receptor, region_receptor, pais_receptor)
            info_envio.append(receptor)

            self.Envios.append((self.Repartidores[repartidor_seleccionado-1], info_envio))
    
    def modificar_envio(self):
        for i in range(len(self.Envios)):
            print(f'Envio N{i+1}° \n{self.Envios[i][0]}\n')
            for j in range(len(self.Envios[i][1])):
                print(f'\n{self.Envios[i][1][j]}\n\n\n')
        envio_seleccionado = int(input('Seleccione un envio: '))
        print(f'Envio N{envio_seleccionado} seleccionado')
        print('1.- Modificar Estado\n2.- Volver al menú\n')
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            nuevo_estado = input('Ingrese el nuevo estado del envío: ')
            self.Envios[envio_seleccionado-1][1][0].estado = nuevo_estado
            print('Estado del envío actualizado correctamente\n')
        elif opcion == 2:
            return

    def listar_envios(self):
        if len(self.Envios) == 0:
            print('No hay envíos registrados')
        else:
            for i, (repartidor, info_envio) in enumerate(self.Envios):
                print(f'Envio N{i+1}°')
                print(f'{repartidor}\n')
                for item in info_envio:
                    print(f'{item}\n')

inicio = True
envios = Envios()
while inicio:
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
            print('No hay envíos registrados')
        else:
            print('Modificar envío')
            envios.modificar_envio()
    elif funcion == 4:
        envios.listar_envios()
    elif funcion == 5:
        inicio = False
    else:
        print('Opción no válida')
