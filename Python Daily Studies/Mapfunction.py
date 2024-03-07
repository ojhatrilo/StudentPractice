# # Define a function that doubles even numbers and leaves odd numbers as is
# def double_even():
#     numans = []
#     num = [1,2,3,34,5]
#     for i in num:
#         if i % 2 == 0:
#             numans.append(i * 2)
#         else:
#             numans.append(i)
#     return numans
#
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
#
# # map() can listify the list of strings individually
# test = tuple(map(list, l))
# print(test)
#
# # Add two lists using map and lambda
#
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))




# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
#     return n + n

#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# Double all numbers using map and lambda

# numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
#
# list1 = list(numbers)
# list2 = list(result)
# dict1 = {}
# for i,j in zip(list1,list2):
#     dict1[i]=j

# print(dict1)













