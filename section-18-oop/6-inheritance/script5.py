from dog import Dog
from cat import Cat
from pig import Pig

dog = Dog("Popi", "dg-1315", "Hembra", "24-10-2008")
dog.show_details()

# Esto solo funciona si comentamos el lanzamiento de la excepción en la
# clase Animal
dog = Dog(chip_number="dg-1315", genre="Hembra", day_birth="24-10-2008")
dog.show_details()