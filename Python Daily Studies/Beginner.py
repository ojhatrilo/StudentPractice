# a = 23
# b = 32
# c = a > b
# print(c)

# Data Types 
# int - numerical values(23)
# Float - Decimal Values (23.432 or 23.0)
# Str  - Any characters or numbers inside the Quotes("hellow")('21')

# Variable rules
# 1. A variable doesn't start with numbers and Special Characters
# 2. A Variabele doesn't contain space
# 3. We can use (_) instead of space
# 4. Special Characters or not used in variables

# Arthimatic operators
# +,-,*,/,//,%,**

# Comparision Operators
# <,>,<=,>=,==,!=

# membership operators
# in
# not in
# a = "my name is Ms.Santhoshni"
# print("Santhoshni" not in a)

# Logical Operators
# and
# or
# not


# Identity Operators
# is 
# is not

# a = int(input("enter the number:"))
# c = float(input("enter the number:"))
# d = input('Enter the name:')


# Type Casting

# a = 23
# print(type(a))
# convert_str = str(a)
# print(type(convert_str))
# convert_int = float(convert_str)
# print(convert_int)
# print(type(convert_int))
# decade = (1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the"
# print(statement,decade)

# Escape Characters
# \n -- New Line
# print("hello my name is \n sanjeev")
# \t -- Tab space
# print("hello my name is\tsanjeev")
# // -- Escapes the character
# print("c:user\\name")
# r -- raw string
# print(r"c:user\name")
# F -- Formated String
# a  = "shri"
# b  = 25
# print(f"\tmy name is \"{a}\"\nMy age is {b}")


# Accessing the characters from the given string
# first_name = "Tharani Kumar"
# single_char = first_name[0]
# print(single_char)

# Accessing the mutiple characters from the given string
# first_name = "Tharani Kumar"
# single_char = first_name[0:7]
# single_char = first_name[::-1]
# print(single_char)
# output (Tharani)
# output (ramuK inarahT)

# Format String
# age  = 18
# print(f"My Age is {age}")

# complex type
# comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# String Methods


# name = "tharani is good"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.replace('good','super'))
# print(len(name))
# print(name.strip())

# Build a menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# name = "tharani is good"
# print(name.startswith("r"))


# #  integer type
# price = 100
# best_price = "hi"
# print(type(price))
# print(isinstance(price, int))

# fl = -32.5
# print(abs(fl))


# String methods
# Join
# split
# upper
# lower
# capitalize
# title
# center
# ljust
# rjust
# replace
# strip
# startswith
# endswith


# Join
# users = ['Dave', 'John', 'Sara']
# print(users)
# z = " ".join(users)
# print(z)
#
# # split
# name = "tharani is good"
# x = name.split()
# print(x)


# List 
# It is used to store multiple items or values in a single variable
# It is ordered, changeable, Allow dupplicates
# To create list  we use "[]"
# It can store multiple datatyes in single Variable
# To convert list we use "list()"


# list1 = [21,"hellow",True,23.5,"hellow"]
# print(list1)

# Acessing the list items
# list1 = [21,"hellow",True,23.5,"hellow"]
# list1[0] = 56
# print(list1[0:4])



# users = ['Dave', 'John', 'Sara','dmmi','anti']
# users.sort(key=str.lower)
# print(users)


# nums = [4, 42, 78, 1, 5]
# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]
# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)
# print(nums)

# a = "Tharani"
# x = list(a)
# print(x)

# List Methods
# Extend -- Join the given two or more list 
# append -- Given valuse can be joined with list
# index -- To find the index value according to the present name
# len -- To define the lenth of the value in the list
# sort -- To arrange the values in asscending
# reverse -- To reverse the list (opposite to oder)
# pop(1) -- To remove last Element in the list
# remove -- To remove dfined name in the list
# delete-- To delete the whole list or indexed value
# clear -- It deletes the entire list
# copy -- It makes duplicate of the present list
# insert -- it is used to insert the vlue in the list

# append
# a = [1,2,3,4,5,"hello"]
# a.append("sir")
# print(a)

# Extend
# a = [1,2,3]
# b = [4,66,7]
# a.extend(b)
# print(a)

# index
# a = [1,2,3,4]
# print(a.index(3))
# print(len(a))

# reverse
# a = [1,2,3,4,5,"hello"]
# a.reverse()
# print(a)

# pop
# a = [1,2,3,4,5,"hello"]
# a.pop(2)
# print(a)

# remove
# a = [1,2,3,4,5,"hello"]
# a.remove(1)
# print(a)



# Tuples
# It is used to store multiple items in a single variable
# It allows duplicates
# It is odered
# It is not changeable or not mutable
# To create tuples "()"
# To convert into tuples we use "tuple()"

# anothertuple = (1, 4, 2, 8, 2, 2)
# x = anothertuple.index(1)
# print(x)

# x = list(anothertuple)
# print(x)
# x.remove(8)
# print(x)
# x.insert(3,10)
# print(x)
# print(anothertuple)
# x[3] = 10
# print(type(x))
# y = tuple(x)
# print(type(y))
# print(anothertuple.index(2))

# Tuples Method
# index
# count

# Sets
# It can store multiple items in a single variable
# Sets are created using "{}"
# Sets doesn't allow duplicates
# Sets are unodered, unchageable, unidexed
# Sets can be converted using "set()"

# thisset = {1,2,3,4,45,6,5,34,33,45,23}
# x = (32 not in thisset)
# print(x)

# nums = {1, True, 2, False, 3, 4, 0}
# print(nums)

# Dictionaries 
# Dictionaries are used to store key,value pairs
# Dictionaries are used to create "{}"
# Dictionaries are odered,changeable, not indexed and 
# Dictionaries do not allow duplicates
# We have nested dictionaries 
 

# Acessing the particular value from the dict
#
# a = {
#     "name":"Ranjani",
#     "age":25,
#     "address":"UK"
# }
# print(a["addresss"])
# print(a.get("ages"))

# # Acessing the keys from the dict
# print(a.keys())

# #  Acessing the values from the dict
# print(a.values())

# # Acessing the key,value pairs from the dict
# x = a.items()
# y = list(x)
# z = y[0]

# print(z)


# # Type check
# print(type(a))

# # verify a key exists
# print('name' in a)

# # Change values
# a["name"] = {"engineer":"SUPER"}
# print(a)
# z = {"engineer":"SUPER"}
# a.update(z)
# print(a)

# # convert to dict
# op = dict(name = "super man", age=1000)
# print(op)

# # Nested dictionaries

# member1 = {
#     "name": "Plant",
#     "instrument": "vocals"
# }
# member2 = {
#     "name": "Page",
#     "instrument": "guitar"
# }
# band = {
#     "member1": member1,
#     "member2": member2
# }
# print(band)
# print(band["member1"]["name"])


# family = {

# "father" : {
# "son":"dasy",
# "wife":"shaerin"
# },
# "grandFather" :{
# "mother":"meena",
# "status":"death"
# }

# }
# print(family["grandFather"])


# if and else condition
# if and else condition are also known as Controlflow 
# (if the)block if condition  becomes true
# Then sequence of  statementes or expression runs under the if block condition
# Else if the if block condition fails eles will be executed

# Types of conditional statements
# if 
# if and else
# nested if and else
# elif  as the same funtion of else

# a = 24
# b = 23
# if a==b:
#     a+=23
#     print(a)
# else:
#     b+=23
#     print(b)

# if b%2==0:
#     print("divisible by 2")
# else:
#     print("not divisible by 2")


# a = int(input("Enter the number:")) 

# if a>0:

#     if a%2 == 0:
#         print("divisible by 2")
#     elif  a%3 == 0:
#         print("divisible by 3")
#     elif a%5 == 0:
#         print("divisible by 5")
#     else:
#         print("not divisible by any number")
    
# else:
#     print("not divisible")


# loops 
# iterating the sequences like string, list, tuple, & sets etc
# types of loops 
# for loop
# while loop

# a =[1,2,3,"hellow"]
# for i in a:
#     print(i)

# Dict loops
# value = {
#     "name":"ojha",
#     "age":23,
#     "phone":1234567890
# }

# for x in value:
#     print(value[x])

# print(value["name"])
# print(value["age"])
# print(value["phone"])

# to find the average of a given list
# list1 = [23,45,32]
# sum = 0
# for i in list 1:
#     sum+=i
# print(sum/len(list1))

#  min =list1[1]
# for i in list1:
#     if i<min:
#         min=i

# print(min)

# list1 = [12,3,45,56,54]
# a = 56
# count = 0-1
# for i in list1:
#     count +=1
#     if a == i:
#         print("value found at index ",count)
# print(count)




















