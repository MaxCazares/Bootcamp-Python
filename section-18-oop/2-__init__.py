class SportInfo:
    """Mostramos información de un deporte"""
    def __init__(self, name):
        print("Estamos creando un objeto")
        self.name = name


run = SportInfo("Correr")
print(run.name)
print(run.__doc__)

swim = SportInfo("Nadar")
print(swim.name)
print(swim.__doc__)