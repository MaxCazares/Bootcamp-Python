# Usando split con valores por defecto (sin parametros)

txt = "Hola soy Maximiliano Cazares"
a = txt.split()                        # ["Hola", "soy", "Maximiliano", "Cazares"]

txt = "python, java, php, c#, kotlin"
a = txt.split(", ")                    # ["python", "java", "php", "c#", "kotlin"]
a = txt.split(", ", 1)                 # ["python", "java, php, c#, kotlin"]
a = txt.split(", ", 2)                 # ["python", "java", "php", c#, kotlin"]

print("Final")