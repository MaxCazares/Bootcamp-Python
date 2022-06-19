txt = "Hola, buenas tardes estamos estudiando el curso de python"

a = txt.find("Hola, ")   #0
a = txt.find("tardes ")  #13
a = txt.find("Hol, ")    #-1

# Añadiendo posición inicial
a = txt.find("Hola, ", 13)    #-1
a = txt.find("tardes ", 10)   #13
a = txt.find("python", -9)    #51

# Añadiendo posición inicial y final
a = txt.find("Hola, ", 0, 3)         #-1
a = txt.find("Hol", 0, 3)            #0
a = txt.find("tardes ", 10, 15)      #-1
a = txt.find("curso de", -19, -5)    #42

print("Final")