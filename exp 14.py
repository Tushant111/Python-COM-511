file_path = "MyFile.txt"

# Ask the user to write three lines and save them to the file
with open(file_path, 'w') as file:
    for i in range(3):
        line = input(f"Enter line {i + 1}: ")
        file.write(line + '\n')

print(f"Lines have been written to {file_path}.")
