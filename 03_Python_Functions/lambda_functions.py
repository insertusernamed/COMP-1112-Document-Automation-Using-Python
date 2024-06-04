# Basic Lambda Function
square = lambda x: x * x
print("Square of 5:", square(5))

# Using Lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers:", squared_numbers)

# Using Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Using Lambda with reduce
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)
