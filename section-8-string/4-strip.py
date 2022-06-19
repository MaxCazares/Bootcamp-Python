# Elimina inicio/final de los caracteres seleccionados

a = "     Hola, Mundo      ".strip()                     # "Hola, Mundo"
a = "     hola    jsjsjsjs    ".strip()                  # "hola    jsjsjsjs "
a = "............ Hola, Mundo ...........".strip(".")    # " Hola, Mundo "
a = "............ Hola, Mundo ...........".strip(". ")   # "Hola, Mundo"
a = "...!!@@@___ Hola, @@ Mundo __--@@.....".strip(". @!-_")   # "Hola, @@ Mundo"
print("Final")