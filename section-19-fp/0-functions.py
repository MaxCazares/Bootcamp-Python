def hello(name = "amig@"):
    return f"¡Hola, {name}!"

def goodbye(name = "amig@"):
    return f"¡Adiós, {name}!"

def message(function,name):
    return function(name)

names = ["Max", "Matz", "Timmy"]

function_hello = hello

for name in names:
    print(message(function_hello,name))

function_goodbye = goodbye

for name in names:
    print(message(function_goodbye,name))