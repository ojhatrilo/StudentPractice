# To Create Fuction we use "def" keyword followed by the name of the function

# def hello():
#     print("iam hello function")
#
# def hi():
#     print("belongs to Hi function")


# hi()
# hello()


#
# def sai():
#     return "iam sai function"
# #
# print(sai())

# def add(num1,num2):
#     return num1+num2
# #
# #
#
# a = input("Enter the number:")
# b = input("Enter the number:")
#
# print(add(a,b))
# print(add(44,23))

# Function Scope
#
# a = 24

# def numacess():
#    global a
#    a+=3
#    print(a)
# #
# numacess()

# Default Argument

# def cyber(num1=3,num2=4):
#    return num1+num2
# #
# print(cyber())
# #

# def multiple_items(*args):
#    print(args)
#    print(type(args))
# #
# #
# multiple_items("Dave", "John", "Sara")
# # #
# def multiple_items(*args):
#    print(args + args)
#    print(type(args))
#
#
# multiple_items(2,6)









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



# # Iterator
# # define a list
# my_list = [4, 7, 0]
# # #
# # # create an iterator from the list
# iterator = iter(my_list)
# #
# # # get the first element of the iterator
# print(next(iterator))  # prints 4
# #
# # # get the second element of the iterator
# print(next(iterator))  # prints 7
# #
# # # get the third element of the iterator
# print(next(iterator))  # prints 0
#


# print(next(iterator))

# # Generator
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
# print(list( my_generator(4)))

    # print each value produced by generator



# Closure is a function having access to the scope of its parent
# function after the parent function has returned.
#

# def parent_function(person, coins):
#     # coins = 3
#
#     def play_game():
#         nonlocal coins
#         coins -= 1
#
#         if coins > 1:
#             print("\n" + person + " has " + str(coins) + " coins left.")
#         elif coins == 1:
#             print("\n" + person + " has " + str(coins) + " coin left.")
#         else:
#             print("\n" + person + " is out of coins.")
#
#     return play_game
#
#
# tommy = parent_function("Tommy", 3) # play_game
# jenny = parent_function("Jenny", 5)
#
# tommy()
# tommy()
# # #
# jenny()
# tommy()




# # Decorator Concept
#
# def make_pretty(func):
#    # define the inner function
#    def inner():
#       # add some additional behavior to decorated function
#       print("I got decorated")
#
#       # call original function
#       func()
#
#    # return the inner function
#    return inner
#
#
# # define ordinary function
# def ordinary():
#    print("I am ordinary")
#
#
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)
#
# # call the decorated function
# decorated_func()



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


# define ordinary function
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#

# decorate the ordinary function

# ordinary()

# call the decorated function





# def hi():
#     print("hi")
#
# def hello():
#     print("iam hello")
#     return hi
#
# se=hello()
# se()




# def add(func):
#     a = 25
#     b = 21
#     c = a+b
#
#     def sub():
#         nonlocal a
#         nonlocal c
#         num1 = c
#         num2 = a
#         z = num1 - num2
#
#         print(z)
#         func(z)
#
#     return sub
# @add
# def mul(a):
#     print(a*5)
#
# mul()







