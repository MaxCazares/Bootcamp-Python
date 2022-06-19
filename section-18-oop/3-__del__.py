class SportInfo:
    """Mostramos información de un deporte"""

    def __init__(self, name):
        print("Estamos creando un objeto")
        self.name = name

    def __del__(self):
        print("Destruyendo el objeto de la clase" + 
        f"{self.__class__.__name__}")


run = SportInfo("Correr")
print(run.name)
print(run.__doc__)

swim = SportInfo("Nadar")
print(swim.name)
print(swim.__doc__)

del run
del swim