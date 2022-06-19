import os
script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/prueba.txt"

# a = añadir información a la anterior
# w = sobrescribir toda la información
# x = crear nuevo fichero (si existe Error)
f = open(file_path, 'a')

input_values = True
while(input_values):
    input_values = input("Texto a almacenar: ")
    if(input_values != "exit"):
        f.write(f'{input_values}\n')
    else:
        input_values = False
        print("Dejamos de añadir información por escribir exit")
f.close()

# Creamos un nuevo fichero
# try:
#     script_directory = os.path.dirname(__file__)    
#     write_text = input("Añadir una palabra: ")
#     file_path = f"{script_directory}/3.txt"
#     f = open(file_path, "x")
#     f.write(write_text + "\n")
#     f.close()
# except Exception as e:
#     print(f"Hubo un error al tratar de crear el fichero: {e}")