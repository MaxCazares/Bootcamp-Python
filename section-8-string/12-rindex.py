txt = "¿Este es el curso de Python? Si, es el curso Bootcamp de Python"

# Valores por defecto

a = txt.rindex("curso")   #39
a = txt.rindex("Python")  #57
a = txt.rindex("python")  #ERROR

# Añadiendo las selecciones

a = txt.rindex("curso", 30)          #39
a = txt.rindex("Python", 0, 10)      #ERROR
a = txt.rindex("Bootcamp", -40, -5)  #45

print("Final")