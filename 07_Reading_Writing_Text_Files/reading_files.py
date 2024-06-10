import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_dir)

# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("Reading the entire file:")
    print(content)

# Reading the file line by line
with open("example.txt", "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line, end="")

# Reading lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nReading lines into a list:")
    print(lines)
