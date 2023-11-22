# 4)Students of District College have a subscription to English and French newspapers.
# Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, 
# and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed
# to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Output Format
# Output the total number of students who are subscribed to the English newspaper only.
# english=set(map(int,input("Roll no of students subscribed to english:").split()))
# french=set(map(int,input("Roll no of French:").split()))
# onlyenglish=len(english-french)
# print(onlyenglish)



# n=int(input("Enter total students of english:"))
# english= set(map(int, input("Enter roll number of English students(seprated by space)").split()))
# m=int(input("Enter total students of french :"))
# french=set(map(int, input("Enter roll number of French students(seprated by space)").split()))
# only_english=len(english-french)
# print("Total number of students who are subscribed to the English newspaper : ",only_english)

n=int(input("Enter the number of students in English subject="))
english=set(map(int,input("Enter the roll number of students that studey English= ").split()))
m=int(input("Enter the number of students in french subject="))
french=set(map(int,input("Enter the rollno of students in english=").split()))
only_english=len(english-french)
print("Roll no of students that study only english newspaper=",only_english)