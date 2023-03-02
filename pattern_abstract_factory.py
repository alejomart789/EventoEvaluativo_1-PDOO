class Celular:
    def __init__(self, modelo, bateria, camara):
        self.modelo = modelo
        self.bateria = bateria
        self.camara = camara

    def __str__(self):
        return f"Celular {self.modelo} con batería de {self.bateria} mAh y cámara de {self.camara} MP."


class CelularSamsung(Celular):
    pass


class CelularApple(Celular):
    pass


class Accesorio:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Accesorio {self.nombre}."


class Funda(Accesorio):
    pass


class ProtectorPantalla(Accesorio):
    pass


class CelularFactory:
    def crear_celular(self):
        pass

    def crear_accesorio(self):
        pass


class SamsungFactory(CelularFactory):
    def crear_celular(self):
        return CelularSamsung("Galaxy S21", 4000, 64)

    def crear_accesorio(self):
        return Funda("Galaxy S21")  


class AppleFactory(CelularFactory):
    def crear_celular(self):
        return CelularApple("iPhone 12", 2815, 12)

    def crear_accesorio(self):
        return ProtectorPantalla("iPhone 12")


# Ejemplo de uso
samsung_factory = SamsungFactory()
apple_factory = AppleFactory()

celular1 = samsung_factory.crear_celular()
accesorio1 = samsung_factory.crear_accesorio()

celular2 = apple_factory.crear_celular()
accesorio2 = apple_factory.crear_accesorio()

print(celular1)
print(accesorio1)

print(celular2)
print(accesorio2)

"""
En este ejemplo, primero creamos una clase base Celular que representa un celular y 
tiene tres atributos: modelo, bateria y camara. Luego, creamos dos clases hijas CelularSamsung y CelularApple
que representan un celular Samsung y un celular Apple, respectivamente. Ambas clases heredan de la clase Celular.

A continuación, creamos una clase base Accesorio que representa un accesorio para celular y tiene un único atributo 
nombre. Luego, creamos dos clases hijas Funda y ProtectorPantalla que representan una funda y un protector de pantalla,
 respectivamente. Ambas clases heredan de la clase Accesorio.

Después, creamos una clase abstracta CelularFactory que representa una fábrica abstracta de celulares y accesorios. 
Esta clase tiene dos métodos abstractos crear_celular y crear_accesorio que deben ser 
implementados por las clases hijas.

A continuación, creamos dos clases hijas SamsungFactory y AppleFactory que representan fábricas concretas de 
celulares y accesorios de Samsung y Apple, respectivamente. Cada una de estas clases implementa los métodos 
crear_celular y crear_accesorio de la clase abstracta CelularFactory para crear objetos concretos CelularSamsung, 
CelularApple, Funda y `ProtectorPantalla
"""