# Tenemos que tener en cuenta:
# Tenemos dos partes: real e imaginaria
# positivo / negativo
# Con o sin decimales
# Ilimitado
# Podemos mostrar un guión bajo para leer los miles
# Podemos trabajar con números científicos

x = 56 + 89j
y = 56.32 + 569.55j
z = 569.32 - 56j

print(type(x))
print(type(y))
print(type(z))
print("Real: "+str(z.real) + " / Imaginario: "+str(z.imag))
print("Final del programa")