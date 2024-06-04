# Creating a tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Accessing elements
print("First coordinate:", coordinates[0])
print("Second coordinate:", coordinates[1])

# Unpacking tuples
x, y = coordinates
print("Unpacked coordinates:", x, y)

# Tuple length
print("Tuple length:", len(coordinates))

# Nested tuples
nested_tuple = (1, (2, 3), 4)
print("Nested tuple:", nested_tuple)

# Iterating over a tuple
print("Iterating over coordinates:")
for coordinate in coordinates:
    print(coordinate)

# Immutable nature of tuples
try:
    coordinates[0] = 30
except TypeError as e:
    print("Error:", e)
