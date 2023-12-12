# Iteration over a List
def iterate_list(my_list):
    print("Iterating over the list:")
    for item in my_list:
        print(item)

# Iteration over a Dictionary
def iterate_dictionary(my_dict):
    print("\nIterating over the dictionary:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

# Get user input for a list
user_list_input = input("Enter a list of elements (comma-separated): ")
user_list = [eval(item.strip()) for item in user_list_input.split(',')]

# Get user input for a dictionary
user_dict_input = input("Enter a dictionary (key1:value1, key2:value2): ")
user_dict = dict(item.split(':') for item in user_dict_input.split(','))

# Demonstrate iteration over the user-input list
iterate_list(user_list)

# Demonstrate iteration over the user-input dictionary
iterate_dictionary(user_dict)
