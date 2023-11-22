matrix = []
row = int(input("Enter how many list you want to add: "))
for i in range(row):
    matrix.append(input("Enter element with space: ").split())

def reverse(mat,k):
    column_values = [m[k] for m in mat]
    column_values.reverse()
    for i in range(len(matrix)):
        matrix[i][k] = column_values[i]
    print(matrix)
    

k = int(input("Enter the column you want to reverse: "))
k -= 1
reverse(matrix,k)