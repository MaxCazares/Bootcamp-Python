# map(función, objeto iterable)

# Obteniedo el doble de cada elemento
def get_doubles(element):
    return element * 2

list_values = [1,2,3,4,5,6,7,8,9,10]

print(list(map(get_doubles, list_values)))
print(list(map(lambda x: x * 2, list_values)))

# Número mayor que 6

def more_than_len_six(word):
    return len(word) > 6

words = ["México", "Argentina", "España", "Colombia"]

print(list(map(more_than_len_six, words)))
print(list(map(lambda x: len(x) > 6, words)))