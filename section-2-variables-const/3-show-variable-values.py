int_value, str_val_one, str_val_two, float_number = 1, "333", "JSJSJS", 2.56

# Variable con texto
print("Primer texto: "+str_val_one)

# Combinación de dos variables
print(str_val_one + str_val_two)

# Combinanción de dos variables de tipo texto
print(int_value + float_number)

# Combinación de dos variables de tipo int y str (ERROR)
print(int_value + str_val_one)

# Este es una alternativa al error anterior
print(str(int_value) + str_val_one) 