txt = "¿Este es el curso de Python? Si, es el curso Bootcamp de Python"

# Valores por defecto

a = txt.count("curso")   #2
a = txt.count("Python")  #2
a = txt.count("python")  #0

# Añadiendo las selecciones

a = txt.count("curso", 30)          #1
a = txt.count("Python", 0, 10)      #0
a = txt.count("Bootcamp", -40, -5)  #1

print("Final")