# To Create Fuction we use "def" keyword followed by the name of the function

# def hello():
#     print("iam hello function")
#
# def hi():
#     print("belongs to Hi function")
#
# hello()
# hi()

#
# def sai():
#     return "iam sai function"
#
# print(sai())

# def add(num1,num2):
#     return num1+num2
#
#
#
# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
#
# print(add(a,b))
# print(add(22,44))

# Function Scope

a = 24

def numacess():
   global a
   a+=3
   print(a)

numacess()

# Default Argument

# def cyber(num1=2,num2=3):
#    return num1+num2
#
# print(cyber(3,5))
#

# def multiple_items(*args):
#    print(args)
#    print(type(args))
#
#
# multiple_items("Dave", "John", "Sara")


# i = 0
# secrets = 5
# while (i<3):
#    num1 = int(input("Enter the number:"))
#    if num1==secrets:
#       print("you win")
#       break
#    else:
#       print("your guess is wrong")
#       i+=1








