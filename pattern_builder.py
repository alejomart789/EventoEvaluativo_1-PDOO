class Pizza:
    def __init__(self):
        self.masa = ""
        self.salsa = ""
        self.toppings = []

    def __str__(self):
        return f"Pizza de {self.masa} con salsa de {self.salsa} y toppings: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_masa(self, masa):
        self.pizza.masa = masa
        return self

    def set_salsa(self, salsa):
        self.pizza.salsa = salsa
        return self

    def agregar_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def construir(self):
        return self.pizza


class Cocina:
    def hacer_pizza(self, builder):
        builder.set_masa("regular").set_salsa("tomate").agregar_topping("queso").agregar_topping("pepperoni")
        return builder.construir()


# Ejemplo de uso
builder_pizza = PizzaBuilder()
cocina = Cocina()

pizza1 = cocina.hacer_pizza(builder_pizza)
print(pizza1)

builder_pizza.set_masa("delgada").set_salsa("barbacoa").agregar_topping("jamón").agregar_topping("cebolla").agregar_topping("pimiento")
pizza2 = builder_pizza.construir()
print(pizza2)


"""
En este ejemplo, primero creamos una clase Pizza que representa una pizza y tiene tres atributos: masa, salsa y toppings. 
Luego, creamos una clase PizzaBuilder que permite construir objetos Pizza de manera más flexible.

La clase PizzaBuilder tiene métodos para establecer la masa, la salsa y agregar toppings a la pizza. 
Estos métodos devuelven el propio objeto PizzaBuilder, lo que permite encadenar llamadas de método 
para construir la pizza de manera más eficiente.

Finalmente, creamos una clase Cocina que es la encargada de construir las pizzas utilizando un objeto PizzaBuilder. 
En este ejemplo, la clase Cocina tiene un único método llamado hacer_pizza, que toma un objeto PizzaBuilder, 
establece algunos atributos de la pizza utilizando los métodos del builder y devuelve la pizza construida.

En el ejemplo de uso, creamos un objeto PizzaBuilder y lo pasamos a la instancia de la clase Cocina para construir 
una pizza. También creamos una segunda pizza utilizando el mismo objeto PizzaBuilder, pero estableciendo 
diferentes atributos.

Cada vez que se llama al método construir del PizzaBuilder, se devuelve un nuevo objeto Pizza 
construido con los atributos establecidos anteriormente.

¡Y eso es todo! Ahora tienes un ejemplo básico de cómo implementar el patrón Builder en
Python para construir objetos Pizza.
"""