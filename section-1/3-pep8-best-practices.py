# Aplicando buenas prácticas Parte 1

# 1.- Uso de la sangría

if 5 > 2:
    print("5 mayor que 2")

# 2.- Código máximo por línea 79 caracteres
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# Código de comentario por línea 72 caracteres máximo

# 3.- Saltos de línea

# 3.1.- Clases


class MyClass:
    # 3.1.1.- Class functions
    def fisrt_function():
        return "first"

    def second_function():
        return "second"

# 3.2.- Principal functions
def principal_function():
    print("principal function")

# 4.- Aplicando lower_snake_case a la función
def second_function():
    print("second function")

# Aplicando en una variable

lower_snake_case_value = 2

# 5.- Clases aplica UpperCamelCase

class SecondClass:
    def _private_function():
        print("private function")

    def public_function():
        print("public function")

# 6.- Sumas
one = 1
two = 2
three = 3
total = ( one
        + two
        - three )
print(total)

one = "1"
two = "34456"
three = "333333"
total = ( one
        + two
        + three )
print(total)