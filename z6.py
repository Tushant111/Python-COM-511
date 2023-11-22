# 6) Write a program to read a list of words and return the longest word.
# Input1:
# 4
# Apple
# Grape
# Kiwi
# Orange
# Output :
#  Orange
list=[]
m=int(input("Total Elements: "))
for i in range(m):
    element=input("Enter the element to insert:")
    list.append(element)
longest_word=""
for j in list:
    if (len(j)>len(longest_word)):
        longest_word=j
print("Longest word is ",longest_word)        
    