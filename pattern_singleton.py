class Hamburguesa:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nombre}: {', '.join(self.ingredientes)}"


class Hamburgueseria:
    instancia = None

    def __new__(cls):
        if not cls.instancia:
            cls.instancia = super().__new__(cls)
            cls.instancia.hamburguesas = []
        return cls.instancia

    def crear_hamburguesa(self, nombre, ingredientes):
        hamburguesa = Hamburguesa(nombre, ingredientes)
        self.hamburguesas.append(hamburguesa)
        return hamburguesa

    def listar_hamburguesas(self):
        return '\n'.join(str(h) for h in self.hamburguesas)


# Ejemplo de uso
hamburgueseria1 = Hamburgueseria()
hamburgueseria2 = Hamburgueseria()

# Verificamos que se trata de la misma instancia
print(hamburgueseria1 is hamburgueseria2)

# Creamos algunas hamburguesas
hamburguesa1 = hamburgueseria1.crear_hamburguesa("Hamburguesa clasica", ["Carne, lechuga, tomate, queso, salsa"])
hamburguesa2 = hamburgueseria1.crear_hamburguesa("Hamburguesa vegana", ["Tofu, lechuga, tomate, aguacate, salsa"])

# Listamos las hamburguesas
print(hamburgueseria2.listar_hamburguesas())