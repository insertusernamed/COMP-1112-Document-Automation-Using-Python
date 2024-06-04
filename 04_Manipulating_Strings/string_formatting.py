# Using f-strings
name = "Daniel"
age = 19
formatted_text = f"My name is {name} and I am {age} years old."
print("Using f-strings:", formatted_text)

# Using format method
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print("Using format method:", formatted_text)

# Using old-style % formatting
formatted_text = "My name is %s and I am %d years old." % (name, age)
print("Using % formatting:", formatted_text)

# Aligning and padding
number = 123.456
print(f"Right-aligned: {number:>10}")
print(f"Left-aligned: {number:<10}")
print(f"Center-aligned: {number:^10}")
print(f"Padded with zeros: {number:010}")
