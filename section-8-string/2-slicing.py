# Selecciona subcadena añadiendo pos. incial / final

uno = "Esto es un curso de python"

a = uno[0:4]     # "Esto"
a = uno[5:10]    # "es un"
a = uno[11:16]   # "curso"
a = uno[17:]     # "de python"

a = uno[-26:-22] # "Esto"
a = uno[-21:-16] # "es un"
a = uno[-15:-10] # "curso"
a = uno[-9:]     # "de python"

a = uno[0:-16]   # "Esto es un"
a = uno[11:-7]   # "curso de"
a = uno[-6:]     # "python"

a = uno[:-22]    # "Esto"
a = uno[:-16]    # "Esto es un"
a = uno[:-10]    # "Esto es un curso"
a = uno[:-7]     # "Esto es un curso de"
a = uno[:]       # "Esto es un curso de python"

a = uno[0:]      # "Esto es un curso de python"
a = uno[5:]      # "es un curso de python"
a = uno[11:]     # "curso de python"
a = uno[17:]     # "de python"

print("Final")