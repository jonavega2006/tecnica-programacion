# HERENCIA: Reutilización de código de una clase padre

class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} puntos de vida")


class Guerrero(Personaje):
    def __init__(self, nombre, vida, espada):
        super().__init__(nombre, vida)
        self.espada = espada

    def mostrar_arma(self):
        print(f"{self.nombre} usa una espada de nivel {self.espada}")


# Uso de la herencia
aragorn = Guerrero("Aragorn", 120, 5)
aragorn.mostrar_vida()
aragorn.mostrar_arma()
