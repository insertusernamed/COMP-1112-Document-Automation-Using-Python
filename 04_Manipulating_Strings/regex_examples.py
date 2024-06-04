import re

# Sample text
text = "The rain in Spain falls mainly in the plain."

# Find all occurrences of a pattern
pattern = r"\bin\b"
matches = re.findall(pattern, text)
print("Occurrences of 'in':", matches)

# Search for a pattern
pattern = r"Spain"
match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")

# Substitute a pattern
pattern = r"rain"
substituted_text = re.sub(pattern, "sunshine", text)
print("Substituted text:", substituted_text)

# Split a string by a pattern
pattern = r"\s"
split_text = re.split(pattern, text)
print("Split text:", split_text)

# Match a pattern at the beginning of the string
pattern = r"^The"
if re.match(pattern, text):
    print("The text starts with 'The'")

# Match a pattern at the end of the string
pattern = r"plain\.$"
if re.search(pattern, text):
    print("The text ends with 'plain.'")
