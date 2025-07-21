print("Basic Calculator")

num1 = float(input("Enter the first number: "))
op = input("Enter the operation: ")
num2 = float(input("Enter the second number: "))

if op == '+':
    result = num1 + num2
    print("Result:", result)

elif op == '-':
    result = num1 - num2
    print("Result:", result)

elif op == '*':
    result = num1 * num2
    print("Result:", result)

elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

elif op == '%':
    if num2 != 0:
        result = num1 % num2
        print("Remainder:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator. Please choose from +, -, *, /, %")
