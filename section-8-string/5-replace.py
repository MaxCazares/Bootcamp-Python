# Reemplazar una subcadena detro de la cadena de texto

str_content = "Hola, esto es un curso de Python_____"

a = str_content.replace("Hola", "Bye Bye")         # "Bye Bye, esto es un curso de Python_____"
a = str_content.replace("Python", "Programación")  # "Hola, esto es un curso de Programación_____"
a = str_content.replace("_", "")                   # "Hola, esto es un curso de Python"

# Remplazamos solo 2 veces
a = str_content.replace("_", "", 2)                # "Hola, esto es un curso de Python___"
a = str_content.replace("_", "", 3)                # "Hola, esto es un curso de Python__"
a = str_content.replace("_", "", 4)                # "Hola, esto es un curso de Python_"
a = str_content.replace("_", "", -5)               # "Hola, esto es un curso de Python"

print("Final")