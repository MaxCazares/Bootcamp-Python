txt = "Hola, buenas tardes estamos estudiando el curso de python"

a = txt.index("Hola, ")   #0
a = txt.index("tardes ")  #13
a = txt.index("Hol, ")    #ERROR

# Añadiendo posición inicial
a = txt.index("Hola, ", 13)    #ERROR
a = txt.index("tardes ", 10)   #13
a = txt.index("python", -9)    #51

# Añadiendo posición inicial y final
a = txt.index("Hola, ", 0, 3)         #ERROR
a = txt.index("Hol", 0, 3)            #0
a = txt.index("tardes ", 10, 15)      #ERROR
a = txt.index("curso de", -19, -5)    #42

print("Final")