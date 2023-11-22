def mini_calculator(a, c, operation):
    if operation == "add":
        return a + c
    elif operation == "sub":
        return a - c
    elif operation == "mul":
        return a * c
    elif operation == "div":
        if c != 0:
            return a / c
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"

while True:
    # Input four numbers
    a_value = float(input("Enter the value of a: "))
    c_value = float(input("Enter the value of c: "))
    x_value = float(input("Enter the value of x: "))
    y_value = float(input("Enter the value of y: "))

    print("Select your operation")
    print("add, sub, mul, div")
    operation_choice = input()

    # Perform the calculation using the mini_calculator function
    if operation_choice in ["add", "sub", "mul", "div"]:
        result = mini_calculator(a_value, c_value, operation_choice)
        print("Result:", result)
    else:
        print("Invalid operation")

    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != "yes":
        break
