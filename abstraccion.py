# ABSTRACCIÓN: Clase base con comportamiento general

class Personaje:
    def __init__(self, nombre, fuerza, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa

    def describir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Defensa: {self.defensa}")


# Uso de la abstracción
goku = Personaje("Goku", 90, 50)
goku.describir()
