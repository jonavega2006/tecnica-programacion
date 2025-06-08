from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_puertas(self):
        print(f"El auto tiene {self.puertas} puertas.")

    # Override transportar
    def transportar(self):
        print(f"El auto {self.marca} {self.modelo} transporta a una familia.")
