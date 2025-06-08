from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_freno):
        super().__init__(marca, modelo)
        self.__tipo_freno = tipo_freno  # privado

    def mostrar_freno(self):
        print(f"La bicicleta tiene frenos de tipo: {self.__tipo_freno}")

    # Override transportar
    def transportar(self):
        print(f"La bicicleta {self.marca} {self.modelo} transporta a una persona.")
