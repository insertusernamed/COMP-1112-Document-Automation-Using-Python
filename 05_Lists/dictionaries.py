# Creating a dictionary
person = {"name": "Daniel", "age": 19, "city": "Cookstown"}
print("Person:", person)

# Accessing elements
print("Name:", person["name"])
print("Age:", person["age"])

# Modifying elements
person["age"] = 30
print("Modified person:", person)

# Adding elements
person["job"] = "Software Engineer"
print("After adding job:", person)

# Removing elements
del person["city"]
print("After removing city:", person)

# Dictionary length
print("Dictionary length:", len(person))

# Iterating over a dictionary
print("Iterating over person:")
for key, value in person.items():
    print(f"{key}: {value}")

# Checking for keys
if "name" in person:
    print("Name is in the dictionary")

# Dictionary methods
keys = person.keys()
values = person.values()
print("Keys:", keys)
print("Values:", values)
