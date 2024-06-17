import subprocess
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Shell commands
# Running a simple command
def run_simple_command():
    result = subprocess.run(
        ["echo", "Hello, World!"], capture_output=True, text=True, shell=True
    )
    print("Output of simple command:")
    print(result.stdout)


# Running a command with arguments
def run_command_with_args():
    try:
        result = subprocess.run(
            ["python", "--version"],
            capture_output=True,
            text=True,
            check=True,
            shell=True,
        )
        print("Python version:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred:")
        print(e.stderr)


# Running a command and capturing its output and errors
def run_command_with_output():
    try:
        result = subprocess.run(
            ["ls"], capture_output=True, text=True, check=True, shell=True
        )
        print("Output of ls -l:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred:")
        print(e.stderr)


# Launching a program (I wrote a simple C program that prints "Hello, World! (Program)")
def run_program():
    # If the operating system is Windows (os.name == 'nt'), use 'hello.exe'
    # Otherwise (for Unix-based systems like Linux or macOS), use './hello'
    executable = "hello.exe" if os.name == "nt" else "./hello"
    subprocess.run([executable])


if __name__ == "__main__":
    run_simple_command()
    run_command_with_args()
    run_command_with_output()

    run_program()
