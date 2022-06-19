import datetime
class Empleado:
    """Mostramos información de una persona"""

    def __init__(self, name, year_birth):
        self.name = name
        self.year_birth = year_birth

    def __str__(self):
        return f"Hola, soy {self.name} y nací en {self.year_birth}"

    def calculate_age(self):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        age = int(year) - self.year_birth
        print(f"{self.name}, esta es tu edad: {age}")


uno = Empleado("Max", 2000)
print(uno)
uno.calculate_age()

dos = Empleado("José", 1985)
print(dos)
dos.calculate_age()