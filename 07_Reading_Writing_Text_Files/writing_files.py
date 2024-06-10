import os

# Getting the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Changing the current working directory to the script's directory
os.chdir(script_dir)

# Writing strings to a file
with open("write_example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Writing a list of strings to a file
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
with open("write_example.txt", "w") as file:
    file.writelines(lines)

# Appending to a file
with open("write_example.txt", "a") as file:
    file.write("Appending a new line.\n")
