# Abrir el fichero especificando nuestra ruta de la carpeta

import os

script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/ejemplo.txt"

# Obtenemos todo el archivo
f = open(file_path)
print(f.read() + "\n")

# Obtenemos 20 caracteres
f = open(file_path)
print(f.read(20) + "\n")

# Obtenemos línea a línea
f = open(file_path)
print("\nlínea 1: " +f.readline())
print("línea 2: " +f.readline())
print("línea 3: " +f.readline())
print("línea 4: " +f.readline() + "\n")

# Obtenemos líne a línea con un for
f = open(file_path)
for line in f:
    print(line)

f.close()