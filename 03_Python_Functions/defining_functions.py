# Basic Function Definition
def greet(name):
    return f"Hello, {name}!"


# Calling the function
print(greet("Daniel"))
print(greet("Jenna"))


# Function with Multiple Arguments
def add(a, b):
    return a + b


print("Sum:", add(3, 5))
print("Sum:", add(10, 20))


# Function with Default Argument
def multiply(a, b=2):
    return a * b


print("Product:", multiply(4))
print("Product:", multiply(4, 3))


# Function Returning Multiple Values
# Using floor devision and modulo operator
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder


q, r = divide(10, 3)
print("Quotient:", q)
print("Remainder:", r)
