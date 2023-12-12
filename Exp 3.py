# Given string
input_string = "Welcome to Python world"

# Count the number of alphabets in the string
alphabet_count = sum(c.isalpha() for c in input_string)
print(f"Number of alphabets in the string: {alphabet_count}")

# Extract characters in the given range (e.g., from index 3 to 10)
start_index = 3
end_index = 10
extracted_characters = input_string[start_index:end_index + 1]
print(f"Characters in the range ({start_index} to {end_index}): {extracted_characters}")

# Check if the string is alphanumeric or not
is_alphanumeric = input_string.isalnum()
print(f"The string is alphanumeric: {is_alphanumeric}")
