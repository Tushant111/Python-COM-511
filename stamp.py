n = int(input("Enter total number of stamp: "))
country_stamp = set()
for i in range(n):
    word = input("Enter: ")
    country_stamp.add(word.lower())

print(country_stamp)