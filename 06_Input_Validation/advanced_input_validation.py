import re


# Using Regular Expressions for Validation
def get_valid_email():
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    """
    Regex to validate an email address:
    ^                : Start of the line
    [a-zA-Z0-9._%+-]+ : Username, 1+ of allowed chars (letters, digits, . _ % + -)
    @                : Literal @ symbol
    [a-zA-Z0-9.-]+   : Domain name, 1+ of allowed chars (letters, digits, . -)
    \.               : Literal dot
    [a-zA-Z]{2,}     : Domain suffix, 2+ letters
    $                : End of the line
    """
    while True:
        user_input = input("Enter an email address: ")
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid email address. Please try again.")


email = get_valid_email()
print("Valid email entered:", email)


# Custom Validation Function
def get_valid_age():
    while True:
        user_input = input("Enter your age: ")
        if user_input.isdigit() and 0 <= int(user_input) <= 120:
            return int(user_input)
        else:
            print("Invalid age. Please enter a number between 0 and 120.")


age = get_valid_age()
print("Valid age entered:", age)
