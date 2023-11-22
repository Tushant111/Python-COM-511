# print("next lin\n \t tab space \n \\")
# def is_palindrome(s):
    
    
#     # Compare the original string with its reverse
#     return s == s[::-1]

# # Input a string to check for palindrome
# input_string = input("Enter a string: ")

# if is_palindrome(input_string):
#     print("It's a palindrome!")
# else:
#     print("It's not a palindrome.")
 
 
 #Now using two pointer approach
def is_palindrome(s): 
    
    left, right = 0, len(s) - 1
    
    while left < right:
        
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    
    return True


input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

