# POLIMORFISMO: Un mismo método se comporta distinto según la clase

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        print(f"{self.nombre} ataca con sus puños")


class Guerrero(Personaje):
    def atacar(self):
        print(f"{self.nombre} ataca con su espada")


class Mago(Personaje):
    def atacar(self):
        print(f"{self.nombre} lanza un hechizo")


# Uso del polimorfismo
lista_personajes = [
    Guerrero("Guts"),
    Mago("Vanessa"),
    Personaje("Aldeano")
]

for p in lista_personajes:
    p.atacar()
