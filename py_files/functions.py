def multiply(a, b):
  return a*b

# A single '/' will yield a float / partial / decimal point having number.
def divide(a, b):
  return a/b

# A double '/' will yield an integer / whole number answer.
def integer_divide(a, b):
  return a//b

def add(a, b):
  return a+b

def subtract(a, b):
  return a-b

def modulo(a, b):
  return a%b

print(multiply(2,5))
print(divide(10,3))
print(integer_divide(10,3))
print(add(2,40))
print(subtract(5,2))
print(modulo(10,3))
