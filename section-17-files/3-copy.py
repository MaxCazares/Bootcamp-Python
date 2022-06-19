import os

script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/ejemplo.txt"
f = open(file_path, "rt")

# Leemos el archivo
copy_file = f.read()

# Creamos un nuevo archivo y escribimos la infomación copiada
f = open(f"{script_directory}/ejemplo_copy.txt", "w")
f.write(copy_file)

f.close()