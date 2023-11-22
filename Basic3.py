# Add elements to a list 
numbers=[21,31,51,11]
print("befor append:",numbers)
#APPend
numbers.append(33)
print("After append",numbers)

even_numbers=[22,34,44,54]
numbers.extend(even_numbers)
print("list after append:",numbers)
# inserting number(INDEX,number)
numbers.insert(20,11)
numbers.insert(0,0)
print("The numbers are",numbers)
numbers.remove(11)
print("The numbers are",numbers)

