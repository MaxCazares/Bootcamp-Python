from functools import reduce

# reduce(función, objeto iterable)

def substraction(total, value):
    return total - value

numbers = list(range(0, 20, 3))
print(numbers)
print(reduce(substraction, numbers))
print(reduce(lambda total, value: total - value, numbers))

def rest_two(total, value):
    return total + value % 2

numbers = list(range(0, 20, 3))
print(reduce(rest_two, numbers))
print(reduce(lambda total, value: total + value % 2, numbers))