# ENCAPSULAMIENTO: Atributos protegidos y control de acceso

class Hechicero:
    def __init__(self, nombre):
        self.__nombre = nombre     # Atributo privado
        self.__mana = 100

    def lanzar_hechizo(self, cantidad):
        if cantidad <= self.__mana:
            self.__mana -= cantidad
            print(f"{self.__nombre} lanza un hechizo de {cantidad} puntos de maná")
        else:
            print("¡No hay suficiente maná!")

    def ver_mana(self):
        print(f"{self.__nombre} tiene {self.__mana} de maná")


# Uso del encapsulamiento
merlin = Hechicero("Merlín")
merlin.ver_mana()
merlin.lanzar_hechizo(30)
merlin.lanzar_hechizo(80)
