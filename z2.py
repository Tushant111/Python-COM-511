# 2)You are given a string S. Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# Input:  qA2
# Output: In the first line, print True if S has any alphanumeric characters. Otherwise, print False
str=input("Enter the sting: ")
alpha_numeric=any(s.isalnum() for s in str)
alphabet=any(s.isalpha()for s in str)
digit=any(s.isdigit()for s in str)
upper=any(s.isupper()for s in str)
lower=any(s.islower()for s in str)
print(alpha_numeric)
print(alphabet)
print(digit)
print(upper)
print(lower)