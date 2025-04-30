# python program to create asimple calculator   

# using functions
#user input
#printresult

def add():
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    result = num1 + num2
    print(f"the sum of {num1} and {num2} is {result}")
    return result
def subtract():
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    result = num1 - num2
    print(f"the difference of {num1} and {num2} is {result}")
    return result
def multiply():
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    result = num1 * num2
    print(f"the product of {num1} and {num2} is {result}")
    return result
def divide():
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    if num2 == 0:
        print("division by zero is not allowed")
        return None
    result = num1 / num2
    print(f"the division of {num1} and {num2} is {result}")
    return result

print("please select an operation:\n" "1. addition\n" "2. subtraction\n" "3. multiplication\n" "4. division")

selection = input("enter your choice (1/2/3/4):")
if selection == '1':
    add()
elif selection == '2':
    subtract()
elif selection == '3':
    multiply()
elif selection == '4':
    divide()
else:
    print("invalid selection")