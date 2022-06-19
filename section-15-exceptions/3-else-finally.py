try:
    print("Ejecutando código")
    list_a = [1]
    print(list_a[1])
except IndexError:
    print("Error en la lista")
except Exception as e:
    print("Algo ha salido mal "+e)
else:
    print("Todo bien, mano")
finally:
    print("Esto se ejecuta aunque haya errores o no")

print("Final")