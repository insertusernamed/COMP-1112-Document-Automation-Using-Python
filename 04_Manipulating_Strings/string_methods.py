# Basic String Operations
text = "   Hello, World!   "
print("Original text:", text)

# Stripping whitespace
stripped_text = text.strip()
print("Stripped text:", stripped_text)

# Converting to uppercase
upper_text = stripped_text.upper()
print("Uppercase text:", upper_text)

# Converting to lowercase
lower_text = stripped_text.lower()
print("Lowercase text:", lower_text)

# Replacing substrings
replaced_text = stripped_text.replace("World", "Python")
print("Replaced text:", replaced_text)

# Splitting strings
words = stripped_text.split()
print("Splitted text:", words)

# Joining strings
joined_text = " ".join(words)
print("Joined text:", joined_text)

# Finding substrings
index = stripped_text.find("World")
print("Index of 'World':", index)

# String length
length = len(stripped_text)
print("Length of text:", length)
