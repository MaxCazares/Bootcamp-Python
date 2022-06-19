# filer(función, objeto iterable)

# Filtrar todos los números enteros

def check_is_int(num):
    return type(num) == int

set = {"max", 1, 2, 2.36, 56+8j}

print(list(filter(check_is_int, set)))
print(list(filter(lambda x: type(x) == int, set)))

# Filtrar todos los elementos con caracteres par

def get_only_even_len(word):
    return len(word) % 2 == 0

words = ["México", "Argentina", "España", "Colombia"]

print(list(filter(get_only_even_len, words)))
print(list(filter(lambda x: len(x) % 2 == 0, words)))

# Filtrar todos los elementos con caracteres impar

def get_only_odd_len(word):
    return len(word) % 2 != 0

words = ["México", "Argentina", "España", "Colombia"]

print(list(filter(get_only_odd_len, words)))
print(list(filter(lambda x: len(x) % 2 != 0, words)))