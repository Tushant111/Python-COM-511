def reverse_kth_rows(matrix, k):
    for i in range(0, len(matrix), k):
        matrix[i:i+k] = matrix[i:i+k][::-1]

# Get user input for the matrix
rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter values for row {i + 1} (comma-separated): ").split(',')))
    matrix.append(row)

# Get user input for k
k = int(input("Enter the value of k: "))

# Reverse every k-th row
reverse_kth_rows(matrix, k)

# Display the modified matrix
print("\nMatrix after reversing every k-th row:")
for row in matrix:
    print(row)
