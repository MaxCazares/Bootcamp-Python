class SportInfo:
    """Mostramos información de un deporte"""
    name = ""

run = SportInfo()
run.name = "correr"
print(run.name)
print(run.__doc__)

swim = SportInfo()
swim.name = "Nadar"
print(swim.name)
print(swim.__doc__)