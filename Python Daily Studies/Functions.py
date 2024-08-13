# To Create Fuction we use "def" keyword followed by the name of the function

# def hello():
#     print("iam hello function")

# def hi():
#     # print("belongs to Hi function")
#     return "satisfied"

# hi = "satisfied"

# print(hi())
# hello()



# def sai():
#     return "iam sai function"
#
#
#
# print(sai())
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# def add():
#     sum = a+b
#     return(sum)

# print(add())
    
# functions with arguments

# def add(a,b):
#     sum = a+b
#     print(sum)

# z = int(input("enter the number:"))
# x = int(input("enter the number:"))
# add(z,x)

# a = input("Enter the number:")
# b = input("Enter the number:")
# 

# print(add(a,b))
# print(add(44,34))

# Function Scope
#
# a = 24

# def numacess():
#    global a
#    a +=33
   
# numacess()
# print(a)

# Default Argument

# def cyber(num1=0,num2=0):
#    return num1+num2

# print(cyber(56,23))



# a = 34
# def groot():
#     s = "super"
#     global a
#     a = 345
#     print(a)
#     return s
#
# groot()
# print(a)


# def multiple_items(*hq):
#    print(hq)
#    print(type(hq))

# multiple_items("Dave", "John", "Sara")



# def multiple_items(*args):
#    print(args[0] + args[2])
#    print(type(args))


# multiple_items(2,6,7)




# print(ord("A"))

# Iterator
# define a list
# my_list = [4, 7, 0, 3]

# # create an iterator from the list
# iterator = iter(my_list)

# get the first element of the iterator
# print(next(iterator))  # prints 4

# # get the second element of the iterator
# print(next(iterator))  # prints 7

# # get the third element of the iterator
# print(next(iterator))  # prints 0

# print(next(iterator)) # prints 3
# print(next(iterator)) # raises StopIteration

# print(next(iterator))
# for i in my_list:
#     print(next(iterator))



# print(next(iterator))

# Generator
# def my_generator(n):

#     # initialize counter
#     value = 0

#     # loop until counter is less than n
#     while value < n:

#         # produce the current value of the counter
#         yield value

#         # increment the counter
#         value += 1

# # iterate over the generator object produced by my_generator
# print(list( my_generator(5)))


    # print each value produced by generator

# def my_function():
#     print("hello")
#
# if __name__ =='__main__':
#     my_function()

#
# def parent_function(person, coins):
#     # coins = 3

#     def play_game():
#         nonlocal coins
#         coins -= 1

#         if coins > 1:
#             print("\n" + person + " has " + str(coins) + " coins left.")
#         elif coins == 1:
#             print("\n" + person + " has " + str(coins) + " coin left.")
#         else:
#             print("\n" + person + " is out of coins.")

#     return play_game


# tommy = parent_function("Tommy", 3) # play_game
# jenny = parent_function("Jenny", 5)


# tommy()
# tommy()
# #
# jenny()
# tommy()




# Decorator Concept

# def make_pretty(func):
#   #  define the inner function
#    def inner():
#       # add some additional behavior to decorated function
#       print("I got decorated")

#       # call original function
#       func()


#   #  return the inner function
#    return inner


# # define ordinary function
# def ordinary():
#    print("I am ordinary")
#    print("Hello Every one")



# # decorate the ordinary function
# decorated_func = make_pretty(ordinary) # inner

# # # call the decorated function
# decorated_func()



# def make_pretty(func):
# #     # define the inner function
#     def inner():
# #         # add some additional behavior to decorated function
#         print("I got decorated")
# #
# #         # call original function
#         func()

#     # return the inner function
#     return inner


# # define ordinary function
# @make_pretty
# def ordinary():
#     print("I am ordinary")

# #
# # @make_pretty
# # def hello():
# #     print("I am hello function")
# # # decorate the ordinary function
# #
# # hello()
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




# def add(q):
#
#     def inner():
#         x = "supper"
#
#         q(x)
#     return inner
#
#
# @add
# def sub(ans):
#     print(ans)

# @add
# def mul():
#     print("decorated")



# sub()
# mul()

























