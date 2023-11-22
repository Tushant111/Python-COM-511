def longestWord():
    str = input("Enter the string separated by comma: ").split(",")
    longest_word = ""
    for i in str:
        if len(i)>len(longest_word):
            longest_word = i
    print(longest_word)
longestWord()



# list = ["orange","mango","demoword"]
# longest_word = ""
# for j in list:
#     if (len(j)>len(longest_word)):
#         longest_word=j
# print("Longest word :",longest_word)