dict1 = {}
dict2 = {}

def input_dict():
    n = int(input("Enter how many numbers you want to add in dict: "))
    for i in range(n):
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        dict1[key] = value

input_dict()
dict2.update(dict1)
input_dict()
dict2.update(dict1)
print(dict2)