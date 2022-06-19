txt = "Hola, esto es un bootcamp de Python"

# Únicamente con la búsqueda de la subcadena

a = txt.startswith("Hola, esto")    #True
a = txt.startswith("Hola, esto es") #True
a = txt.startswith("Hola, estoes")  #False
a = txt.startswith("hola, esto")    #False

# Especificando rangos

a = txt.startswith("Hola, esto",10)    #False
a = txt.startswith("esto es", 6)       #True
a = txt.startswith("esto es", 6, 10)   #False
a = txt.startswith("bootcamp", 17, 25) #True

print("Final")