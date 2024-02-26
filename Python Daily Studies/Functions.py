# To Create Fuction we use "def" keyword followed by the name of the function

# def hello():
#     print("iam hello function")
#
# def hi():
#     print("belongs to Hi function")
#
# hello()
# hi()

# def sai():
#     return "iam sai function"
#
#
# print(sai())

# def add(num1,num2,num3):
#     return num1+num2
#
#
#
# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
#
# print(add(a,b,3))

# Function Scope

# a = 24
#
# def numacess():
#    global a
#    a+=3
#    print(a)
#
# numacess()

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



# Iterator
# # define a list
# my_list = [4, 7, 0]
#
# # create an iterator from the list
# iterator = iter(my_list)
#
# # get the first element of the iterator
# print(next(iterator))  # prints 4
#
# # get the second element of the iterator
# print(next(iterator))  # prints 7
#
# # get the third element of the iterator
# print(next(iterator))  # prints 0


# Generator
# def my_generator(n):
#
#     # initialize counter
#     value = 0
#
#     # loop until counter is less than n
#     while value < n:
#
#         # produce the current value of the counter
#         yield value
#
#         # increment the counter
#         value += 1
#
# # iterate over the generator object produced by my_generator
# for value in my_generator(3):
#
#     # print each value produced by generator
#     print(value)


# Decorator Concept

# def make_pretty(func):
#     # define the inner function
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")
#
#         # call original function
#         func()
#
#     # return the inner function
#     return inner
#
#
# # define ordinary function
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
#
# # decorate the ordinary function
#
# ordinary()

# call the decorated function

















