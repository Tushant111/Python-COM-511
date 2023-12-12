def demonstrate_type_checking_and_functions(data):
    # Type checking
    print(f"Type of the data: {type(data)}")

    # Using built-in functions
    if isinstance(data, (int, float)):
        print(f"Absolute value: {abs(data)}")
        print(f"Rounded value: {round(data)}")

    if isinstance(data, (str, list, tuple)):
        print(f"Length of the data: {len(data)}")
        if all(char.isalnum() for char in data):
            print("All characters are alphanumeric.")
        else:
            print("Not all characters are alphanumeric.")

    if isinstance(data, (list, tuple)):
        print(f"Minimum value: {min(data)}")

# Get user input for data
user_input = input("Enter data (could be an integer, float, string, list, or tuple): ")

# Demonstrate type checking and functions for the user input
demonstrate_type_checking_and_functions(eval(user_input))
