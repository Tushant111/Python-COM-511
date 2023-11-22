# very basic
#name=90 name is a variable here



# print("hello putarr") #prints function
# a=20.5
# b=30
# c="45"
# # print(a+b)
# print(int (a)) #conversion of float to int
# print(type(c))

#STRING OPERATORS
#CONCATINATION
# str1="hello"
# str2="brother"
# print(str1+str2)
# concatination=str1+str2
# print(concatination)

#REPEATATION
# str1="hello \n"
# print(str1 * 3)

#Less smaller
# a="Apple"
# b="Banana"
# if a>b:
#  print("yes")
# else:
#     print("No")
# a="appleeeeeeeee"
# b="Banana"
# if a>b:
#  print("Greater") #its is showing smaller and greater onn the basis of a comes first then comes b
# elif a<b:
#     print("Smaller")
# elif a==b:
#     print("Equal")

 #find the substring in str
# str1="hello this is vivek"
# print(str1.find("this"))

#WHILE LOOP
# count=3
# while (count<5):
#  count=count+1
#  print("hello")

#list
# L=[12,20,3,5,"harry",2.5] 
# print(type(L))
# L[0]="Strange" #to change elements at 0 index
# L.append(10)#add an elemnt to the list
# L.remove(3) #remove an elemnt from the List
# L.insert(9, 'Shanu') #insert an element at any index using insert
# #u have three methoda to add using insert,append and defaulkt L[index]=element
# print(L)
# print(L[1])
# print(len(L)) #it gives the number of elemnts in list

# list=['Hello',1,4,'Raju','alkat']
# # list(5)="kudi" we can not use this we have to use insert to insert between
# list.insert(2, 'sakina')
# print(list)
# liist=[1,5,4,3,78]
# liist.sort() #here sorting can only be used in a list that can contain either string or either list only
# #to print reverse of a list liist.sort(reverse=True)
# print(liist)

#Lists are always mutable i.e the values inside the List can be changed.
#If we dont want to change the values inside the list we can use tuples

#Tuples
# tuple=(10,11,"hello",45,"brither",10)
# print(type(tuple))
# #here the only diff between tuple and list is that tuple is immutable
# print(tuple[0])
# print(tuple.count(10)) #to count how many time 10 is inserted

#dictionary
# dict1={}
# dict1["vivek"]=100
# print(dict1)
# dict={
#    "car":"4 wheeler",
#    "Brand":"Mustang,ferrari,Alto",
#    "MModel":"201"
#  }

# print(dict)
# print(dict.items())#used to print the items
# marks={'hindi':10,'Eng':20,'Math':90}
# print(marks['Eng'])
# print(marks.get('science')) #so get is used to get the result without an error if we would have used print(marks['science])
# #then output would be an error
# marks['Sci']=100
# print(marks)


#set
#A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
# set={10,20,"hell"}
# print(type(set))
# print(set) # Sets are unindexed so they can come in any form in output

# True and 1 is considered the same value and same values are ignored:

# thisset = {"apple", "banana", "cherry", True, 1, 2,0,False}

# print(thisset)
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)
#thisset={} is empty dictionary and thisset=set(()) is an empty set
# set={'mon','tue','wed'}
# set.add('thu')
# print(set)


# #converting a list to set
# list=['mon','tue','wed','mon']
# # print(list)
# sett=set(list)
# print(sett) 


#taking input from user
# marks=input("enter your marks")
# print(f"Your marks are {marks}")

# a=int(input("enter the number a"))
# b=int(input("enter the number b"))
# sum=a+b
# print(f"Sum is:{sum}")

#functions
#it is a block of code that performs some task and runs when it is called
# def greetings():
#     print("hello how are you")
    # greetings() #here the function is called when this is qriteen then the output is shown


# def greetings(user):
#     print(f"hello {user} how are you")
# for i in range(1,4):
#  greetings("Ram")

# def greetings(user,age):
#     print(f"hello {user} how are you,your age is{age}")
# for i in range(1,4):
#  greetings("Ram",56)

