#  Write a Python program to implement a linear search algorithm to find the position of a specific element in a list.
# Prompt the user to enter a list of numbers and a target value to search for. If the target value is found, print its 
# position; otherwise, print a message indicating that the value is not in the list.And print all occurrences of the target
# value in the list along with their Positions.

# Input1 : 
# First line     - given list as “n”
# Second line - target
# Output 1:
# Find the target element and print the index position of the target  
list=[]
index=[]
n=int(input("Enter the number of elements in list"))
for i in range (n):
     num=int(input("Enter the number:"))
     list.append(num)
element=int(input("Enter the element to find in list:"))
for j,item in enumerate(list):
    if item==num:
        index.append(j)
if index==[]:
    print("Element not found")
else:
  print("Element found:")
    