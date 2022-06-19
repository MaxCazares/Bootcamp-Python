txt = "Hola, esto es un bootcamp de Python"

# Únicamente con la búsqueda de la subcadena

a = txt.endswith("de Python")           #True
a = txt.endswith("bootcamp de Python")  #True
a = txt.endswith("bootcampde Python")   #False

# Especificando rangos

a = txt.endswith("de Python", 15)               #True
a = txt.endswith("bootcamp de Python", 17)      #True
a = txt.endswith("bootcamp de Python", 17, -6)  #False

print("Final")