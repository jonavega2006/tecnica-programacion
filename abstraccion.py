class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

    def transportar(self):
        print(f"El vehículo {self.marca} {self.modelo} está listo para transportar.")
