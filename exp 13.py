def get_unique_words(file_path):
    unique_words = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Removing punctuation marks and converting to lowercase
                    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
                    unique_words.add(cleaned_word)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return set()

    return sorted(unique_words)

# Get user input for the file path
file_path = input("Enter the path to the text file: ")

# Get and print unique words in alphabetical order
unique_words = get_unique_words(file_path)

if unique_words:
    print("\nUnique words in alphabetical order:")
    for word in unique_words:
        print(word)
else:
    print("No unique words found.")
