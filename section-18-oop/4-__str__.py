class Empleado:
    """Mostramos información de una persona"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hola, soy {self.name} y tengo {self.age}"


uno = Empleado("Max", 21)
print(uno)

dos = Empleado("Hose", 32)
print(dos)