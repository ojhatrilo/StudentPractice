# a = "Hello"
# b = "world"
# c = a+b
# print(c)

# a = 200
# b = 200
# x = a>=b
# y = b>=a
# z = a==b
#
# print(x)
# print(y)
# print(z)

# a = 'hellow world'
# x =list(a)
# y = len(x)
# print(y)

# list1 = ["apple",'babanaa']
# print(len(list1[0]))
# print(len(list1[1]))

# a = ["apple"]
# x = tuple(a)
# print(x)

# a = 100
# b = 99
# if a < b :
#     b+=20
#     if a < b :
#         a+=40
#         if a > b :
#             print(a,b)
#         else:
#             print('#')
#     else:
#         print('#')
# else:
#     print('#')

# prime number to
# a = 12
# if a%2 == 0:
#     print('not a prime')
# elif a%3 == 0:
#     print('not a prime')
# elif a%5 == 0:
#     print('not a prime')
# elif a%7 == 0:
#     print('not a prime')
# elif a%11 == 0:
#     print('not a prime')
# else:
#     print('prime')

# x = '21'
# y = int(x)
# print('value of y:',y)
# print('value of x:',x)
#
# print('value of y:',type(y))
# print('value of x:',type(x))

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:
# f = open('C:\\Users\\Hey!\\Desktop\\today.txt')
# x = f.read()
# z = ''
# for i in x :
#     if i not in x:
#         print(i)
#
# f.close()


# file input & output

# input = open('C:\\Users\\Hey!\\Desktop\\today.txt', 'r')
# output = open('demo2.txt', 'w')
# text = input.read()
# print(type(text))
# z = text.split()
# y = []
# 
# for i in z:
#     if "Lorem"== i :
#         e=i.replace('Lorem','nayak')
#         y.append(e)
#     else:
#         y.append(i)
# 
# x = str(y)
# print(x)
# output.write(x)
# input.close()
# output.close()
# 
# import numpy as np
#
# arr = np.array([1, 2, 3, 4], ndmin=5)
#
# print(arr)
# print('number of dimensions :', arr.ndim)

# list1 = ['adrew','willams','sagar',21,3.1]
#
# capword = []
# num = []
# for i in list1:
#     if type('a')==type(i):
#         z = i.capitalize()
#         capword.append(z)
#     else:
#         num.append(i)
#
# print(capword)
# print(num)
# thistuple = ('hellow', 'how', 23, True)
# x = ('ragav',)
# z = thistuple+x
# print(z)


# swap the given tuple position[0] -> <- position[2]
# char1 = ('hellow', 'how', 'rajesh')
# list1 = list(char1)
# temp = list1[0]
# list1[0] = list1[2]
# list1[2] = temp
# x = tuple(list1)
# print(x)

#change or replace the value called hellow to the your name
# to convert tuple use tuple keyword ex:tuple()
# char2 = ('hellow', 'how', 'rajesh')

# sets are unodered
# sets not indexed
# sets don't allow dupplicates
# they are not accesible through index number
# to create sets we use {}
# to convert sets we use keyword called "set()"
# we can add ste items using their element name
# we cna remove set items using their element name
# it can store multiple values in a single variable

# Dictionaries they dont allow duplicates
# Dictioaries are odered
# Dictionaries are changeable
# Dictionaries dont contain index number
# Dictionaries are created using '{}'
# Dictionaries are converted using 'dict()'
# Dictionaries are used to store multiple items in a single variable
# Dictionaries store the valuse in the form of key value pairs

# Dictionary Example
# dict1 = {
#     'name':'raj',
#     'age': 23,
#     'phone no': 72123312412,
# }
# dict1['id'] = 12
# print(dict1)


# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#     print(x)



# #
# import numpy as np
#
# a = [[1,3,4],
#      [2,5,8],
#      [7,6,3]]
#
# b = [[2,8,9],
#      [4,3,6],
#      [5,4,2]]
#
# c = np.dot(a,b)
# print(c)





# details = {
#
#     1:{"name":"hardik","age":24,"post":"player"},
#     2:{"name":"suresh","age":17,"post":"umpire"}
#
# }
#
# def name():
#     for i in details:
#         print(details[i]["name"])
#
# name()






















