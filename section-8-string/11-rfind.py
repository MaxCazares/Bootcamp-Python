txt = "¿Este es el curso de Python? Si, es el curso Bootcamp de Python"

# Valores por defecto

a = txt.rfind("curso")   #39
a = txt.rfind("Python")  #57
a = txt.rfind("python")  #-1

# Añadiendo las selecciones

a = txt.rfind("curso", 30)          #39
a = txt.rfind("Python", 0, 10)      #-1
a = txt.rfind("Bootcamp", -40, -5)  #45

print("Final")