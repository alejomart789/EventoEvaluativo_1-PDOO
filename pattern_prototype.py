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