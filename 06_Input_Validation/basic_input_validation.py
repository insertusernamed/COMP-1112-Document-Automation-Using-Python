# Validating Numeric Input
def get_valid_number():
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")


number = get_valid_number()
print("Valid number entered:", number)


# Validating String Input
def get_valid_string():
    while True:
        user_input = input("Enter a non-empty string: ")
        if user_input.strip():
            return user_input
        else:
            print("Invalid input. Please enter a non-empty string.")


string = get_valid_string()
print("Valid string entered:", string)
