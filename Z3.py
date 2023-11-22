# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 
# She asked for your help. You pick the stamps one by one from a stack of  country stamps.
# Find the total number of distinct country stamps ?
# Input Format :
# The first line contains an integer N, the total number of country stamps.
# The next N lines contain the name of the country where the stamp is from.
# Output Format :
# Output the total number of distinct country stamps on a single line.
list=[]
n=int(input("Enter the total number of country stamps:"))
for i in range(n):
    m=input("Enter the name of the country:")
    list.append(m)
print(list,len(list))
    