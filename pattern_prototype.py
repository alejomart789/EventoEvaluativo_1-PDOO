import copy

class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.color})"

    def clone(self):
        return copy.deepcopy(self)


class FabricaCarros:
    def __init__(self):
        self.carros = {}

    def agregar_carro(self, nombre, carro):
        self.carros[nombre] = carro

    def obtener_carro(self, nombre):
        return self.carros[nombre].clone()


# Ejemplo de uso
fabrica_carros = FabricaCarros()

# Creamos algunos carros
carro1 = Carro("Toyota", "Corolla", "Rojo")
carro2 = Carro("Ford", "Mustang", "Negro")

# Los agregamos a la fábrica de carros
fabrica_carros.agregar_carro("Corolla rojo", carro1)
fabrica_carros.agregar_carro("Mustang negro", carro2)

# Clonamos algunos carros
carro_clonado1 = fabrica_carros.obtener_carro("Corolla rojo")
carro_clonado2 = fabrica_carros.obtener_carro("Mustang negro")

# Verificamos que son diferentes objetos
print(carro1 is carro_clonado1)
print(carro2 is carro_clonado2)

# Verificamos que los clones tienen los mismos atributos que los originales
print(carro1)
print(carro_clonado1)

print(carro2)
print(carro_clonado2)

"""
En este ejemplo, la clase Carro representa un carro y la clase FabricaCarros es el prototipo 
que se encarga de crear y almacenar los diferentes tipos de carros. La implementación del patrón Prototype 
se hace en el método clone de la clase Carro, que se encarga de crear una copia profunda del objeto carro.

Luego, se puede utilizar la fábrica de carros para crear clones de los diferentes tipos de carros con el 
método obtener_carro. La fábrica de carros utiliza el método clone de la clase Carro para crear una copia 
profunda del objeto carro y así obtener un nuevo objeto con los mismos atributos que el objeto original.

De esta manera, se pueden crear diferentes tipos de carros en la fábrica de carros y clonarlos para 
obtener nuevos objetos con los mismos atributos que los objetos originales.
"""