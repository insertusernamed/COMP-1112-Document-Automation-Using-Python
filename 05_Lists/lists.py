# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying elements
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Removing elements
fruits.remove("apple")
print("After remove:", fruits)

# List length
print("List length:", len(fruits))

# List slicing
print("Slicing first two elements:", fruits[:2])

# Iterating over a list
print("Iterating over fruits:")
for fruit in fruits:
    print(fruit)

# List comprehension
squared_numbers = [x**2 for x in range(5)]
print("Squared numbers:", squared_numbers)
