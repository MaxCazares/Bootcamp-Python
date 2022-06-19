# variables globales sin ahacer uso de la palabra global

# Primer caso: solo con variable global
variable_global = "Hola, Mundo"

def custom_function():
    print(variable_global)

print("Fuera: "+variable_global)
custom_function()

# Segundo caso: variable global y variable local
variable_global = "save me, pls"

def custom_function():
    variable_global = "Kill me, pls"
    print(variable_global)

print("Fuera: "+variable_global)
custom_function()

# Haciendo uso de la palabra clave "global"

name = "Sue-Metal"
def use_global_function_value():
    global name 
    name = "BabyMetal"

print(name)
use_global_function_value()
print("este es el nombre: "+name)