# def armstrong(num):
#     st = str(num)
#     length = len(st)
#     total = sum(int(digit) ** length for digit in st )
#     return total



# n = int(input("Enter the number: "))
# if armstrong(n) == n:
#     print("Armstrong")
# else:
#     print("Nope")
    
def armstrong(num):
    st=str(num)
    length=len(st)
    total=sum(int(digit) ** length for digit in st )
    return total
num=int(input("Enter:"))
if armstrong(num) =='num':
    print("armstrong")
else:
    print("nahi ha")