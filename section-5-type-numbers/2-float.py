# Tenemos que tener en cuenta:
# positivo / negativo
# Con decimales
# Ilimitado
# Podemos mostrar un guión bajo para leer los miles
# Podemos trabajar con números científicos

# Básico
x = 12.356
y = -889.656
z = 5657.567891210000000000000
a = 20_000_000.565_689
b = 0.000_000_565_565

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

# Mostrar el resultado de forma más legible 
real = 4.0400000000000000000045
real_string = f'{real:.2f}'
print(real_string)

# Números científicos
x = 345.56e3
y = 12e-5
z = -784.55e100
print("Final del programa")