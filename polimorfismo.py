from vehiculo import Vehiculo
from bicicleta import Bicicleta
from auto import Auto

def main():
    vehiculos = [
        Bicicleta("Trek", "FX 3", "disco"),
        Auto("Toyota", "Corolla", 4),
        Vehiculo("Genérico", "Modelo X")
    ]

    for v in vehiculos:
        v.describir()
        v.transportar()
        print("-" * 30)

    bici = vehiculos[0]
    if isinstance(bici, Bicicleta):
        bici.mostrar_freno()

    auto = vehiculos[1]
    if isinstance(auto, Auto):
        auto.mostrar_puertas()

if __name__ == "__main__":
    main()
