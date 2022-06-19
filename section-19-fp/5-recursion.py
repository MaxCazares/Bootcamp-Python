# Descontador

# Con un for
# for i in range(20, 0, -1):
#     print(i)

# Con recursividad
from typing import Reversible


def discount_value(value):
    if value <= 0:
        return
    else:
        print(value)
        return discount_value(value - 1)

discount_value(20)

# Factorial de un número

# Con un for
result = 1
n = 5
for i in range(1, n + 1):
    result *= i

print(f"{n}! = {result}")

# Con recursividad

def factorial_number(n):
    return n * factorial_number(n - 1) if n > 1 else 1

factorial = 6

print(f"{factorial}! = {factorial_number(6)}")