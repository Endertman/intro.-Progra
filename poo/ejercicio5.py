class Motocicleta:
    def __init__(self, color, matricula, combustible_litros, numero, ruedas, marca, fecha_fabricacion, peso, cilindrada, motor):
        self.marca = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero = numero
        self.ruedas = ruedas
        self.marca = marca
        self.fecha_fabricacion = fecha_fabricacion
        self.peso = peso
        self.cilindrada = cilindrada
        self.motor = motor
    
    def arrancar(self):
        if self.motor == True:
            print("El motor ya esta en marcha")
        else:
            self.motor = True
            print("El motor se ha arrancado")

    def detener(self):
        if self.motor == False:
            print("El motor ya esta detenido")
        else:
            self.motor = False
            print("El motor se ha detenido")


moto = Motocicleta("roja", "1234", 10, 2, 2, "yamaha", "2020-01-01", 100, 150, False)
moto.arrancar()
moto.detener()
moto.detener()
moto.arrancar()
moto.arrancar()
