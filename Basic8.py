for i in range(1, 51):
    a = i
    c = i + 1
    
    print(f"Numbers: a={a}, c={c}")
    
    print("Select your operation")
    print("add, sub, mul, div")
    b = input()
    
    if b == "add":
        print("add:", a + c)
    elif b == "sub":
        print("Sub:", a - c)
    elif b == "mul":
        print("mul:", a * c)
    elif b == "div":
        if c != 0:
            print("div:", a / c)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid")
