import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_dir)

# Check if the file exists before attempting to open it
file_path = "example.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
else:
    print(f"{file_path} does not exist.")

# Writing to a file using context manager
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Appending to a file using context manager
with open("output.txt", "a") as file:
    file.write("Appending a new line.\n")

# Further appending to a file using context manager
with open("output.txt", "a") as file:
    file.write("Appending another line using context manager.\n")
