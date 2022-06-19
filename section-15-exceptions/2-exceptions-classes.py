try:
    print("jsjsjsjs")
    list_one  = ["uno", "dos", "tres"]
    numbre_one = float(input("introduce un numero 1: "))
    numbre_two = float(input("introduce un numero 2: "))
    division = numbre_one/numbre_two
    print(list_one[1])
    del list_one
    print(list_one[1])
except KeyboardInterrupt:
    print("\nHas presionado ctrl + c, ojo papá")
except NameError:
    print("Alguna variable no existe")
except IndexError:
    print("Este indice no existe")
except ZeroDivisionError:
    print("ojo división entre cero")
except ValueError:
    print("No podemos introducir un string en valor númerico")
except Exception as excep:
    print(excep)

print("Final")