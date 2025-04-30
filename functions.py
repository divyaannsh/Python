# # Functions

# a function is block of code that performs a a specific task
# # A function is defined using the def keyword

# def greetings():
#     print("welcome tot he python course by rishabh")


# # # calling a function

# greetings()


# create a function that takes two numbers as arguments and returns their sum
# def add_numbers(num1, num2):
#     return num1 + num2
# print("the sum",add_numbers(5, 10))


# def add_numbers(num1,num2,num3):
#     return num1 + num2 + num3

# print("the sum of three numbers is",add_numbers(5,10,15))

# add_numbers(5,14,15)

# def add2num(a,b):

#     return a+b

# print("the sum of two numbers is",add2num(5,10))

def ceslsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temcelsius = float(input("enter the temperature in celsius"))
fahrenheit = ceslsius_to_fahrenheit(temcelsius)
print(f"the temperature in fahrenheit is {fahrenheit}")