class Avion:
    def __init__(self, nombre, velocidad, alcance):
        self.nombre = nombre
        self.velocidad = velocidad
        self.alcance = alcance

    def __str__(self):
        return f"Avión {self.nombre} - Velocidad: {self.velocidad} km/h, Alcance: {self.alcance} km"


class AvionComercial(Avion):
    def __init__(self):
        super().__init__("Boeing 737", 840, 6055)


class AvionCarga(Avion):
    def __init__(self):
        super().__init__("Airbus A330-200F", 871, 7400)


class AvionPrivado(Avion):
    def __init__(self):
        super().__init__("Cessna Citation XLS+", 833, 3411)


class AvionEjecutivo(Avion):
    def __init__(self):
        super().__init__("Gulfstream G550", 904, 12000)


class FabricaAviones:
    def crear_avion(self, tipo):
        if tipo == "comercial":
            return AvionComercial()
        elif tipo == "carga":
            return AvionCarga()
        elif tipo == "privado":
            return AvionPrivado()
        elif tipo == "ejecutivo":
            return AvionEjecutivo()
        else:
            raise ValueError(f"Tipo de avión no válido: {tipo}")


# Ejemplo de uso
fabrica_aviones = FabricaAviones()

# Creamos un avión comercial
avion_comercial = fabrica_aviones.crear_avion("comercial")
print(avion_comercial)

# Creamos un avión de carga
avion_carga = fabrica_aviones.crear_avion("carga")
print(avion_carga)

# Creamos un avión privado
avion_privado = fabrica_aviones.crear_avion("privado")
print(avion_privado)

# Creamos un avión ejecutivo
avion_ejecutivo = fabrica_aviones.crear_avion("ejecutivo")
print(avion_ejecutivo)

# Intentamos crear un avión con un tipo no válido
try:
    avion_no_valido = fabrica_aviones.crear_avion("no_valido")
except ValueError as e:
    print(str(e))


"""
En este ejemplo, la clase Avion representa un avión genérico y las clases AvionComercial 
y AvionCarga representan aviones comerciales y de carga, respectivamente. 
La clase FabricaAviones es el Factory Method que se encarga de crear instancias 
de aviones según el tipo especificado.

En el método crear_avion de la clase FabricaAviones, se utiliza una estructura condicional 
para determinar qué tipo de avión debe crear. Si el tipo es "comercial", 
se crea un objeto de la clase AvionComercial, y si el tipo es "carga", se crea un objeto de la clase AvionCarga.
 Si se especifica un tipo no válido, se lanza una excepción.

Luego, se puede utilizar la fábrica de aviones para crear instancias de aviones según el tipo deseado. 
En este ejemplo, se crean un avión comercial y un avión de carga utilizando la fábrica de aviones.
"""