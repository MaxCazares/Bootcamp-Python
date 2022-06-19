import os
file_to_remove = input("Nombre del archivo a borrar: ")
try:
    script_directory = os.path.dirname(__file__)
    file_path = f"{script_directory}/{file_to_remove}"
    if(os.path.exists(file_path)):
        os.remove(file_path)
        print(f"{file_to_remove} fue borrado exitosamente")
    else:
        print(f"El fichero {file_to_remove} no exite")
except Exception as general_exception:
    print(f"Hubo problemas con los ficheros {general_exception}")