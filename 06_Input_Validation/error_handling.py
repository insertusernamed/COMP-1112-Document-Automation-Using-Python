# Using try-except to Handle Invalid Input
def get_number_with_error_handling():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


number = get_number_with_error_handling()
print("Valid number entered:", number)


# Combining Validation and Error Handling
def get_positive_number():
    while True:
        user_input = input("Enter a positive number: ")
        try:
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


positive_number = get_positive_number()
print("Valid positive number entered:", positive_number)
