# Haciendo uso de f-string

# Añadiendo variables interpolado dentro del string
course = "Python"
name = "max Cazares"
a = f"Nombre del curso: {course}. Alumno: {name}"  
# Nombre del curso: Python. Alumno: max Cazares"

# Expresiones dentro de las interpolaciones

a = f"{12+12+4+5}"    #33
a = f"{12+12*(4+5)}"  #120

a = f"{name.lower()}"       # max cazares
a = f"{name.capitalize()}"  # Max Cazares

# Usando caracteres de escape
    
a = f"Hola soy \'{name}\'. \nEstoy haciendo el curso de \'{course}\'"

print("Final")