str = input("Enter the string: ")

def check(str):
    for i in str:
        count = str.count(i)
        if count!= ord(i)-ord('a') + 1:
            return False
    return True
print(check(str))