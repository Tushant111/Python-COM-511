
#1
# def merge_dict(dict1,dict2):
#     merged={**dict1, **dict2}
#     print(merged)
# dict1={}
# dict2={}
# n=int(input("Enter the number of items in dict1 : "))
# for i in range(n):
#     key=input("Enter Key : ")
#     value=input("Enter value: ")
#     dict1[key]=value
# m=int(input("Enter the number of items in dict2 : "))
# for j in range(m):
#     key=input("Enter Key : ")
#     value=input("Enter value: ")
#     dict2[key]=value
# merge_dict(dict1,dict2)

#  or atul
#WAP to add two dictionaries
# dict1 = {}
# dict2 = {}
# newdict = {}

# def inputdict():
#     n = int(input("Enter the number of values you want to insert: "))
#     for i in range(n):
#         key = input("Enter the key: ")
#         value = input("Enter the value of the key: ")
#         dict1[key] = value
#     m = int(input("Enter the number of values you want to insert: "))
#     for i in range(m):
#         key = input("Enter the key: ")
#         value = input("Enter the value of the key: ")
#         dict2[key] = value

# inputdict()

# newdict.update(dict1)
# newdict.update(dict2)

# # # Now you can print newdict outside the function to see the final result
# print(newdict)






# # 2

# str=input("Enter your string: ")
# alphanumeric=any(s.isalnum() for s in str)
# alphabetical=any(s.isalpha() for s in str)
# digits=all(s.isdigit() for s in str)
# lowercase=any(s.islower() for s in str)
# uppercase=any(s.isupper() for s in str)
# print(alphanumeric)
# print(alphabetical)
# print(digits)
# print(lowercase)
# print(uppercase)




# # 3
# n=int(input("Enter The Total number of country stamps : "))
# country_stamp=set()
# for i in range(n):
#     country_name=input("Enter the "+ str(i+1) +" country stamp Name : ")
#     country_stamp.add(country_name.lower())
# print("Total Number Of Distinct Country Stamps : ",len(country_stamp))


# or

# n = int(input("Enter the total number: "))
# list = set()
# for i in range(n):
#     country = input("Enter country name: ")
#     list.add(country.upper())

# print(list,len(list))


# # 4
n=int(input("Enter total students of english:"))
english= set(map(int, input("Enter roll number of English students(seprated by space)").split()))
m=int(input("Enter total students of french :"))
french=set(map(int, input("Enter roll number of French students(seprated by space)").split()))
only_english=len(english-french)
print("Total number of students who are subscribed to the English newspaper : ",only_english)





# # 5
# list=[]
# index=[]
# n=int(input("Enter Number of Elements in List = "))
# for i in range (n):
#     num=int(input("Enter element ="))
#     list.append(num)
# element=int(input("Enter Elements to find in list = "))
# for j,item in enumerate(list):
#     if item == element:
#         index.append(j)
# if index==[]:
#     print("The target value ",element," is not in the list.")
# else:
#     print("The target value ",element,"  is found at positions:",index)

# or 

# list = []
# index = []

# def linearSearch():
#     n = int(input("Enter how many numbers you want to add in the list: "))
#     for i in range(n):
#         list.append(int(input("Enter: ")))  #to add number at last of list

#     target = int(input("Enter the value ou want to search: "))

#     for i,j in enumerate(list):
#         print(i,j)
#         if j == target:
#             index.append(i)

# linearSearch()

# print(index)




# #6
# list=[]
# n=int(input("Enter Number of Elements in List = "))
# for i in range (n):
#     num=input("Enter element =")
#     list.append(num)
#     print(list)

# longest_word=""
# for j in list:
#     if (len(j)>len(longest_word)):
#         longest_word=j
# print("Longest word :",longest_word)



# #7

# matrix=[[11,12,13]
#         ,[14,15,16]
#         ,[17,18,19]]

# print("Original Matrix : ")
# for row in matrix:
#     print(row)

# k=int(input("Enter kth column = "))

# k=k-1


# column_values = []

# for row in matrix:
#     print(row)
#     column_values.append(row[k])

# reversed_column=list(reversed(column_values))

# for i in range(len(matrix)):
#     matrix[i][k]=reversed_column[i] 


# print("Original Matrix : ")
# for row in matrix:
#     print(row)

# or 

# def reverse(matrix, k):
#     k -= 1  # Adjust k to be zero-based index
#     column = [row[k] for row in matrix]  # Extract the k-th column
#     column.reverse()  # Reverse the extracted column
#     for i in range(len(matrix)):
#         matrix[i][k] = column[i]  # Replace the original column with the reversed column

# matrix = []
# row = int(input("Enter how many list you want to add: "))
# for i in range(row):
#     matrix.append(input("Enter element with space: ").split())

# print(matrix)
# k = 1
# reverse(matrix, k)

# for row in matrix:  
#     print(row)
 
 #or
 
# matrix = []
# row = int(input("Enter how many list you want to add: "))
# for i in range(row):
#     matrix.append(input("Enter element with space: ").split())



# #8
# str = input("Enter the string: ")

# def check(str):
#     for i in str:
#         count = str.count(i)
#         if count!= ord(i)-ord('a') + 1:
#             return False
#     return True
# print(check(str))

# EASY LEVEL

# 1.Write a Python program to implement a linear search algorithm to find the position of a specific element in a list. Prompt the user to enter a list of numbers and a target value to search for. If the target value is found, print its position; otherwise, print a message indicating that the value is not in the list.And print all occurrences of the target value in the list along with their positions.

# TESTCASES:
# 1  2  3  2  5  2 6  
# Input1:
#   2
# Output1: The target value 2  is found at positions: [1,4,5]

# Input2:
#   8
# Output2 : The target value 8 is not in the list.

# 2.write a program to read a list of words and return the longest word. 

# Testcases:

# Input :

# First line     -list size as ‘n’
# Second line - elements 

# Output :

# Print longest word

# Eg:    
# 4 
# 	Apple
# 	Grape
# 	Kiwi
# 	Orange 
# Output :
# 	Orange 

# 3.Write a program to check the given integer is Armstrong number or not.
# Test casae:
# 	Input 1:
# 		First line - given inters as “n”
# 	Output 1:
# 		The given number is Armstrong or not
# Eg :
# 	Input 1:
# 		153
# 	Output1:
# 		The given integer is  an Armstrong.


# 	Input 2;
# 		170
# 	Out put 2:
# 		The given integer is  not an Armstrong.


# 4.Write a program to merge 2 dictionary 
# Testcases :

# Out put1:
# 	Merge dictionary
# Eg :

# Input 1:(program defined input )

# dict1={"a":85,"b":89}
# dict2={"b":69,"c":78}


# 	Output1:
# {'a': 85, 'b': 69, 'c': 78}







# HARD LEVEL
# 1.Write a program to reverse  k-th column in a matrix

# TESTCASES:
# Input 1:

# 11   12   13
#     14   15   16
# 17   18   19 
# Column no:1

# Output 1:

# 17   12   13
#     14   15   16
# 11   18   19 

# 2.write a program to create a mini calculator to perform the arithmetic operations only.(Only using by functions ) //[+ ,- , *, / ,%]
# Testcases :
# 	Input1:
# 		First line     - num1
# 		Second line - num2
# 		Third line    - user choice among this [+ ,- , *, / ,%]
# 	Out put 1
# 		Performed output
# Eg:	input1:
# 		27
# 		77
# 		+
# 	Output1:
# 		104
# 	Input2:
# 		20
# 		56
# 		!
# 	Output2:
# 		Invalid choice 
# # Function to perform addition
# def add(x, y):
#     return x + y

# # Function to perform subtraction
# def subtract(x, y):
#     return x - y

# # Function to perform multiplication
# def multiply(x, y):
#     return x * y

# # Function to perform division
# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero"
#     return x / y

# # Function to calculate the remainder (modulus)
# def modulus(x, y):
#     if y == 0:
#         return "Cannot divide by zero"
#     return x % y

# # Main program
# x = float(input("Enter the first number: "))
# y = float(input("Enter the second number: "))

# print("Available operations:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")
# print("5. Modulus (%)")

# choice = input("Select an operation (1/2/3/4/5): ")

# if choice == '1':
#     result = add(x, y)
#     operation = "Addition"
# elif choice == '2':
#     result = subtract(x, y)
#     operation = "Subtraction"
# elif choice == '3':
#     result = multiply(x,y)
#     operation = "Multiplication"
# elif choice == '4':
#     result = divide(x,y)
#     operation = "Division"
# elif choice == '5':
#     result = modulus(x,y)
#     operation = "Modulus"
# else:
#     result = "Invalid choice"
#     operation = "Unknown operation"

# print(f"{operation} result: {result}")



# 3.Write a program to print the index values and   count vowels ( Case sensitive) in given Strings.
# Testcases:
# 	Input 1:
# 		First line - enter the string 
# 	Output1:
# 		Index position of all vowels and total count 


# Eg:
# 	Input 1:
# 		Apple 
# 	Output1:
# 		0 ,4 , number of vowels - 2 




# 4.Write a program to remove duplicates elements in a given list.

# Test cases:
# 	Input1:
# 		First line - given list
# 	Output1:
# 		List of unique elements
# Eg:
# 	Input1:
# 		pen , pencile , scale, rubber, pen , scketch pencil ,scale
# 	Output1:
# 		pen , pencile , scale, rubber, scketch pencil 

 




















# MCQ

# 1. Operators with the same precedence are evaluated in which manner?

# a) Left to Right
# b) Right to Left
# c) Can’t say
# d) None of the mentioned
# Ans: a

# 2. What is the output of the given below program?
# x = 5
# y = x -= 3
# print(y)
# a) 8
# b) 2
# c) None
# d) Error
# Ans : D
# 3) What will be the output of the following Python code?
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
 
#     i + = 1
# a) 1 2 3
# b) error
# c) 1 2
# d) none of the mentioned
# Ans:b
# Explanation: SyntaxError, there shouldn’t be a space between + and = in +=.

# 4) What will be the output of the following code?
# x = 5
# x += "2"
# print(x)
# 7	B. 52	 C. Error	D. 72

# Answer: C
 
# 5) What are the values of the following Python expressions?
# 2**(3**2)
#  (2**3)**2
#  2*3*2
# a) 512, 64, 512
# b) 512, 512, 512
# c) 64, 512, 64
# d) 64, 64, 64
# Answer: a
# Explanation: Expression 1 is evaluated as: 2*9, which is equal to 512. Expression 2 is evaluated as 82, which is equal to 64. The last expression is evaluated as 2(3*2). This is because the associativity of ** operator is from right to left. Hence the result of the third expression is 512.
# 6) What is the output of bool("False")?
# A. True
# B. False
# C. None
# D. "False"
# Answer: A 
# 7) What will be the output of the following Python program?
# z=set('abc')
# z.add('san')
# z.update(set(['p', 'q']))
# z
# a) {‘a’, ‘c’, ‘c’, ‘p’, ‘q’, ‘s’, ‘a’, ‘n’}
# b) {‘abc’, ‘p’, ‘q’, ‘san’}
# c) {‘a’, ‘b’, ‘c’, ‘p’, ‘q’, ‘san’}
# d) {‘a’, ‘b’, ‘c’, [‘p’, ‘q’], ‘san}
# Answer: c
# Explanation: The code shown first adds the element ‘san’ to the set z. The set z is then updated and two more elements, namely, ‘p’ and ‘q’ are added to it. Hence the output is: {‘a’, ‘b’, ‘c’, ‘p’, ‘q’, ‘san’}
# 8) Which of the following is a feature of Python DocString?
# a) In Python all functions should have a docstring
# b) Docstrings can be accessed by the _doc_ attribute on objects
# c) It provides a convenient way of associating documentation with Python modules, functions, classes, and methods
# d) All of the mentioned
# Answer: d
# Explanation: Python has a nifty feature called documentation strings, usually referred to by its shorter name docstrings. DocStrings are an important tool that you should make use of since it helps to document the program better and makes it easier to understand.
# 9) What is the output of the code 7 // 3?
# A. 2.33
# B. 2
# C. 3
# D. 2.0


# Answer: B
# 10) What will be the output of the following Python code?
# i = 2
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 2
# a) 2 4 6 8 10 …
# b) 2 4 
# c) 2 3
# d) error
# Answer: b
# Explanation: The numbers 2 and 4 are printed. The next value of i is 6 which is divisible by 3 and hence control exits the loop.


# 11) Why are local variable names beginning with an underscore discouraged?
# a) they are used to indicate a private variables of a class
# b) they confuse the interpreter
# c) they are used to indicate global variables
# d) they slow down execution
# Answer: a
# Explanation: As Python has no concept of private variables, leading underscores are used to indicate variables that must not be accessed from outside the class.


# 12) The output of which of the codes shown below will be: “There are 4 blue birds.”?
# a) ‘There are %g %d birds.’ %4 %blue
# b) ‘There are %d %s birds.’ %(4, blue)
# c) ‘There are %s %d birds.’ %[4, blue]
# d) ‘There are %d %s birds.’ 4, blue
# Answer: b
# Explanation: The code ‘There are %d %s birds.’ %(4, blue) results in the output: There are 4 blue birds. When we insert more than one value, we should group the values on the right in a tuple.

# 13) What will be the output of the python code shown below for various styles of format specifiers?
# x=1234
# res='integers:...%d...%-6d...%06d' %(x, x, x)
# res
# a) ‘integers:…1234…1234  …001234’
# b) ‘integers…1234…1234…123400’
# c) ‘integers:… 1234…1234…001234’
# d) ‘integers:…1234…1234…001234’
# Answer: a
# Explanation: The code shown above prints 1234 for the format specified %d, ‘1234  ’ for the format specifier %-6d (minus ‘-‘ sign signifies left justification), and 001234 for the format specifier %06d. Hence the output of this code is: ‘integers:…1234…1234  …001234’
# 14) What will be the output of the following Python code snippet?


# x=3.3456789
# print('%f | %e | %g' %(x, x, x))
# a) Error
# b) ‘3.3456789 | 3.3456789+00 | 3.345678’
# c) ‘3.345678 | 3.345678e+0 | 3.345678’
# d) ‘3.345679 | 3.345679e+00 | 3.34568’
# Answer: d
# Explanation: The %f %e and %g format specifiers represent floating point numbers in different ways. %e and %E are the same, except that the exponent is in lowercase. %g chooses the format by number content. Hence the output of this code is: ‘3.345679 | 3.345679e+00 | 3.34568’.
# 15) What will be the output of the following Python code?
# print(0xA + 0xB + 0xC)
# a) 0xA0xB0xC
# b) Error
# c) 0x22
# d) 33
# Answer: d
# Explanation: 0xA and 0xB and 0xC are hexadecimal integer literal representing the decimal values 10, 11 and 12 respectively. Their sum is 33.
# 16) What will be the output of the following Python code snippet?


# print('0xa'.isdigit())
# a) True
# b) False
# c) None
# d) Error
# Answer: b
# Explanation: Hexadecimal digits aren’t considered as digits (a-f).
# 17) What will be the value of x in the following Python expression, if the result of that expression is 2?x>>2
# a) 8
# b) 4
# c) 2
# d) 1
# Answer: a
# Explanation: When the value of x is equal to 8 (1000), then x>>2 (bitwise right shift) yields the value 0010, which is equal to 2. Hence the value of x is 8.
# 18)  To find the decimal value of 1111, that is 15, we can use the function:
# a) int(1111,10)
# b) int(‘1111’,10)
# c) int(1111,2)
# d) int(‘1111’,2)
# Answer: d
# Explanation: The expression int(‘1111’,2) gives the result 15. The expression int(‘1111’, 10) will give the result 1111.
# 19) What will be the value of the following Python expression?


#  bin(10-2)+bin(12^4)

# a) 0b10000
# b) 0b10001000
# c) 0b1000b1000
# d) 0b10000b1000
# Answer: d
# Explanation: The output of bin(10-2) = 0b1000 and that of bin(12^4) is ob1000. Hence the output of the above expression is: 0b10000b1000.
# 20) What will be the output of the following Python code snippet?
# a = [0, 1, 2, 3]
# for a in a:
#     print(a)


# a) 0 1 2 3
# b) 0 1 2 2
# c) 3 3 3 3
# d) error


# Answer: a
# Explanation: The value of a[0] changes in each iteration. Since the first value that it takes is itself, there is no visible error in the current example

# Debugging Questions on Python

# 1. What will be the output of the following pseudocode?therwise 
#      What will be the output of the following pseudocode?
# Initialize Integer x, y, z
# Set y = 1, x = 2  
# z = x ^ y
# Print z
# a)1           b)  2          c)    4              d)  3
# option-d
# Explanation: 
# Firstly variables x, y, and z are initialized, then y and x are assigned values 1 and 2 respectively.
# Now z is assigned the value of x XOR y i.e. 1 ^ 2 = 3. Since all bits in 1 and 2 are exclusive so the XOR will be equal to 1 OR 2 i.e. 3

# 2.Which of the following series will be printed by the given pseudocode? 
# Integer a, b, c 
# Set b = 0, c = 0 
# for(each a from 1 to 5) 
#   print c 
#   b = b + 1 
#   c = c + b 
# end for
# a)5 4 3 2 1      b)0  1   3   6   10     c)2  5  8  9  10    d)0 0 0 0 0
# option-2
# Explanation: 
# Firstly variables a, b, and c are initialized, then b and c are assigned values 0 and 0 respectively.
# Now run a loop from 1 to 5, in each iteration b is incremented by 1, and c is incremented by b.
# In the first iteration print c = 0 value of b is incremented by 1 i.e. b = 1, c is incremented by b i.e. c = 1
# In the second iteration print c = 1 value of b is incremented by 1 i.e. b = 2, c is incremented by b i.e. c = 3
# In the third iteration print c = 3 value of b is incremented by 1 i.e. b = 3, c is incremented by b i.e. c = 6
# In the fourth iteration print c = 6 value of b is incremented by 1 i.e. b = 4, c is incremented by b i.e. c = 10
# In the fifth iteration print c = 10 value of b is incremented by 1 i.e. b = 5, c is incremented by b i.e. c = 15
# Thus the final series is 0 1 3 6 10
# 3. What is the output?
# Integer a, b, c
# Set c = 12, b = 4
# a = c / b
# c = b >> a
# Print c
# a)2      b)0      c)6       d)4
# Option-b
# Explanation: 
# Initial value of c = 12 and b = 4 
# Then a = c/b = 12/4 = 3 
# Now c = b(4) right shift by a(3) = 0
# 4. Predict the output of the following pseudo-code 

# Integer x = 1, y = 2, z = 3 
# x = y + z 
# z = x – y 
# z = z + x 
# z = y + z 
# y = y + z 
# Print x, y, z
# a)1 2 3      b)4 6  8     c)5 12 10   d)8 6 10
# Option-3
# Explanation: 
# Value of x is y + z = 2 + 3 = 5 
# Value of z changes to x - y = 5 - 2 = 3 then z= z + x = 3 + 5 = 8 then z = y + z = 2 + 8 = 10 then y = y + z = 2 + 10 = 12 
# Thus x = 5, y = 12, z = 10

#  5)What will be the output of the following pseudocode 
# for input a = 30, b = 60, C = 90?

# Integer a, b, c, sum 
# Read a, b, c 
# Set sum = a + b + c 
# if ((sum EQUALS 180) and (a NOT EQUALS 0) and 
# (b NOT EQUALS 0) and (c NOT EQUALS 0))
#      Print " Success" 
# Otherwise 
#      Print "Fail" 
# End if

# Options: 

# 1)Success     2)fall        3)compilation error      4)none of the mentioned

# Correct option :1

# Option_1

# Explanation :

# a = 30, b = 60, C = 90
# sum=180
# ((sum EQUALS 180) and (a NOT EQUALS 0) and (b NOT EQUALS 0) and (c NOT EQUALS 0))
# So, (true) and (true) and (true) and (true)
# So, output will be "success"


# 6)What will be the output of the following pseudo-code?

# integer i
# set i=3
# do
# print i+3
# i=i-1
# while( i !< 0)
# end while

# Options:

# 1)6 5 4          2)6 4 2           3)3 2 1           4)1 2 3

# Correct option:
# Option_1

# Explanation:

# Step 1:
# It will print i+3, here i value is 3. So i+3 is 6. On the next line, i will be decremented by 1. Then check
# the conditions in do-while() i!=0. Here updated i value is 2 (2!=0),so condition is true. The loop continues.

# Step 2:
# It will print i+3, here updated i value is 2. So i+3 is 5. On the next line I will be decremented by 1. Then
# checking the conditions in do-while() i!=0. Here updated i value is 1 (1!=0),so condition gets true. The
# loop continues

# Step 3:
# It will print i+3, here updated i value is 1. So i+3 is 4. On the next line, I will be decremented by 1. Then
# check the condition in do while() i!=0. Here updated i value is 0 (0!=0), so the condition gets false.
# Thus the loop gets terminated!
# 7)How many times the following loop will be executed?

# main()

# {

#   ch = ‘b’;

#   while(ch >= ‘a’ && ch <= ‘z’)

#   ch++;

# }

# Options:

# 1)compilation                       2)25                  3)26          4)1

# Correct option:
# option_2

# Explanation:

# The loop will execute for 25 time.
# First iteration : b lie between a to z. Then ch=c;
# Second iteration : c lie between a to z. Then ch=d;
# similarly it will run till ch=z
# 8)What will be the output if limit = 6?
# Read limit
# n1 = 0, n2= 1, n3=1, count = 1;
# while count <= limit
# count=count+1
# print n3
# n3 = n1 + n2
# n1 = n2
# n2 = n3
# End While
# Options 
# 1)112358         2)124532             3)14523            4)231456
# Correct option:
# Option_1
# Explanation:
# First iteration of while loop: count <= limit. 1<=6. So, we will enter while loop.  count=2, Now we will print n3. So value of n3 is 1. 1 will be printed. n3=n1+n2. So, n3=1,n1=1,n2=1
# Second iteration: Count=3, Print n3. So 1 will be printed , n3=2, n1=1, n2=2
# Third iteration: Count=4, Print n3. So 2 will be printed , n3=3, n1=2,  n2=3
# Fourth iteration: Count=5 , Print 3, n3=5, n1=3, n2=5
# Fifth iteration: Count=6, Print 5, n3=8, n1=5, n2=8
# Sixth iteration: Count=7, Print 8, n3=13, n1=8, n2=13
# Hence output will be 112358.
# 9. What will be the output of the following Python code? 
# x = 50
#  def func(x): 
# print('x is', x)
#  x = 2 
# print('Changed local x to', x)
#  func(x)
#  print('x is now', x)


# OPTIONS:
# 1.x is 50 Changed local x to 2 x is now 50
# 2.x is 50 Changed local x to 2 x is now 2
# 3.x is 50 Changed local x to 2 x is now 100
# 4.NONE OF THE ABOVE
# CORRECT:
# OPTION_2
# EXPLANATION:
# The global statement is used to declare that x is a global variable – hence, when we assign a value to x inside the function, that change is reflected when we use the value of x in the main block.
# 10.What will be the output of the following Python code? 
# def maximum(x, y):
#  if x > y:
#  return x
#  elif x == y: 
# return 'The numbers are equal' 
# else: return y 
# print(maximum(2, 3))
# OPTIONS:
# 1.2
# 2.3
# 3.The numbers are equal 
# 4.None of the mentioned
# CORRECT:
# OPTION_2
# EXPLANATION:
# The maximum function returns the maximum of the parameters, in this case the numbers supplied to the function. It uses a simple if..else statement to find the greater value and then returns that value.
