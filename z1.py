# #Joining two dictionaries

# 1) Write a program for Merging two Dictionaries

# dict1={}
# dict2={}
# newdict={}
# def inputdict():
#     n=int(input("enter the number of keys you want to insert in dictionary 1:"))
#     for i in range(n):
#         key=input("enter the key:")
#         value=input("enter the value:")
#         dict1[key]=value
#     print(dict1)
#     m=int(input("enter the number of elents to insert in dict 2:"))
#     for i in range(m):
#         key=input("enter the key:")
#         value=input("enter the value:")
#         dict2[key]=value
#     print(dict2)
# inputdict()
# newdict.update(dict1)
# newdict.update(dict2)
# print(f"updated dictionary is{newdict}")

#without functuon
# dict1={}
# dict2={}
# newdict={}
# # def inputdict():
# n=int(input("enter the number of elements you want to insert in dict1"))
# for i in range(n):
#      key=input("enter the key")
#      value=input("enter the value")
#      dict1[key]=value
# m=int(input("enter the number of elements you want to insert in dict2"))
# for i in range(m):
#      key=input("Enter the key:")
#      value=input("Enter the value:")
#      dict2[key]=value
# # inputdict()
# newdict.update(dict1)
# newdict.update(dict2)
# print(f"new dictionary is {newdict}")
     

d={}
d1={}
new={}
def insert():
    n=int(input("enter the number of elements u want to enter="))
    for i in range(n):
        key=input("enter the key=")
        value=int(input("Enter the value"))
        d[key]=value
    m=int(input("enter the number of elements u want to enter="))
    for i in range(m):
        key=input("enter the key=")
        value=int(input("Enter the value"))
        d[key]=value
insert()
new.update(d)
new.update(d1)
print(new)