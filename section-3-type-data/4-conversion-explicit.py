# int
s = "101011010"
# Conversión del string a entero base 2
c = int(s, 2)
print("String converted to int base 2: ", c)
# Conversión del string a entero base 10
c = int(s)
print("String converted to int base 10: ",c)

# str
print("int => string: ", str(10))
print("float => string: ",str(34.43))
print("complex = string: ",str(45+5j))

# list
print("String => list: ",list('anitalavalatina'))
print("int (a str) => list:", list(str(78)))
print("tuple = list", list(tuple("palindromo")))

# set
print("String => set: ", set('anitalavalatina'))
print("int (a str) => set:", set(str(88)))
print("tuple = set", set(tuple("palindromo")))

# hexadecimal
s = 18
c = hex(s)
print("valor hexadecimal de {}: {}".format(s, c))

# octal
s = 18
c = oct(s)
print("valor octal de {}: {}".format(s, c))