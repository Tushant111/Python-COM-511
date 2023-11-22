mat = []
row = int(input("Enter how many list you want to add: "))
for i in range(row):
    mat.append(input("Enter element with space: ").split())
j=1
l=len(mat)-1
for i in range(len(mat)//2):
    mat[i][j-1],mat[l-i][j-1]=mat[l-i][j-1], mat[i][j-1]
print(mat)