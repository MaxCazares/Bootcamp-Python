# 1 - Comillas simples
a = "Hola \'Mundo, esto esta de locos\'"
print("1 - "+a)

# 2 - Saltos de linea
a = "A: Hola \nB: Hola \nA: jsjsjs"
'''
A: Hola
B: Hola
A: jsjsjs
'''
print("2 - "+a)

# 3 - Tabulación
a = "A: Hola \tB: Hola \tA: jsjsjs"
# "A: Hola    B: Hola    A: jsjsjs"
print("3 - "+a)

# 4 - Retroceso
a = "Hola\b"     #Hola
print("4 - "+a)
a = "Hola\bt"    #Holt
print("4 - "+a)
a = "Hola\b\bty" #Hoty
print("4 - "+a)

# 5 - Contra barra
a = "C:\\nuevo-doc"  #C:\nuevo-doc
print("5 - "+a)
a = "C: \nuevo-doc"  
'''
C:
uevo-doc
'''
print("5 - "+a)

print("Final")