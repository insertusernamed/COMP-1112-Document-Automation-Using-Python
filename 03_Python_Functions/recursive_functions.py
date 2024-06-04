# Factorial Function Using Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))


# Fibonacci Function Using Recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
