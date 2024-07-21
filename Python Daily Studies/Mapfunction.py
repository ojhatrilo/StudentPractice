# # Define a function that doubles even numbers and leaves odd numbers as is
# def double_even(n):
#
#     # num = [1,2,3,34,5]
#     # for i in num:
#     if n % 2 == 0:
#         return n*2
#     else:
#         return  n

# print(double_even())

# Create a list of numbers to apply the function to
# numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
# result = list(map(double_even, numbers))

# # Print the result
# print(result)  # [1, 4, 3, 8, 5]
#
#
#
#
# List of strings
# l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
# test = map(list, l)
# print(list(test))

# Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# #
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))




# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
#     if n % 2 == 0:
#         return n+n
#     else:
#         return n
# #
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# Double all numbers using map and lambda

# numbers = {1, 2, 3, 4}
# result = map(lambda x: x + x, numbers)
#
# print(list(result))
#
# list1 = list(numbers)
# list2 = list(result)
# dict1 = {}
# for i,j in zip(list1,list2):
#     dict1[i]=j
# #
# print(dict1)

# # number of elements
# n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function

# print("\nList is - ", a)
#
# a = map(int,input("enter the ele:").split())
# print(list(a))

# n = int(input("Enter the number of elements to be stored:"))
# a = input("enter the element:").split()
#
# if len(a) == n:
#     a = map(int,a)
#     print(list(a))
# else:
#     print("length is not satisfied")


# list1 = []
# n = int(input("Enter the number of elements to be stored:"))
#
# for i in range(n):
#     a = int(input("Enter the number:"))
#     list1.append(a)
# print(list1)


# list1 = [24,34,56,78,89]

# def hello(n):
#     return n+2

# x = map(hello,list1)
# print(list(x))



# list1 = [22,52,45,56,34]

# for i in list1:
#     print(i)

# list1 = [25,32,56,78]
# list2 = []
# for i in list1:
#     list2.append(i+2)
# print(list2)

# def hello(n):
#     return n+2

# maptut = map(hello,list1)
# print(list(maptut))





