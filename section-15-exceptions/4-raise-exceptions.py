try:
    print("Ejecutando código")
    pos_index = 8
    list_a = [1, 2, 3, 4, 5, 6]
    if len(list_a) - 1 < pos_index:
        raise IndexError (f"El indice seleccionado es {pos_index}"
        f" y la longitud de la lista es {len(list_a)}")
except IndexError as ee:
    print("Algo ha ido mal ")
    print(ee)
except Exception as e:
    print("Algo ha salido mal ")
    print(e)
else:
    print("Todo bien, mano")
finally:
    print("Esto se ejecuta aunque haya errores o no")

print("Final")