# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# #
# print(mydoubler(11))
# print(mytripler(11))

# x = lambda a: a + 10
# print(x(5))


# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# print(mydoubler(11))


# a =  lambda a,b,c:a+b+c
#
# num1= input()
# num2= input()
# num3= input()
# print(a(num1,num2,num3))



# add = lambda a,b : a+b
# sub = lambda a,b : a-b

# print(sub(23,45))
# 
# while(True):
#     options = input("enter option:")
#     num1 = int(input("enter the number:"))
#     num2 = int(input("enter the number:"))
#     if options == "1":
#         print(add(num1,num2))
#     elif options =='2':
#         print(sub(num1,num2))
#     else:
#         break


# original_tuple=(1,2,3,4,5)
# reversed_tuple=original_tuple[::-1]
# print("original_tuple:",original_tuple)
# print("reversed_tuple:",reversed_tuple)


# t1=input("Enter the numbers:")
# t2=input("Enter the numbers:")
# tem=t1
# t1=t2
# t2=tem
# print(t1,t2)

# a=[1,2,3,4,5,6,7,8,9]
# l=len(a)
# tot=0
# for i in range(l):
#   tot=tot+a[i]
# print(tot)
#

# str1=input("Enter the string:")
# str2=str1[1:].replace(str1[1],'$')
# print(str1[0]+str2)



# def add(x, y):
#   return x+y;
#
# print(add(10,20))
#
#
# def add(*x):
#   a= 0
#   for i in x:
#     a+=i
#   return a
#
# print(add(1,2,3,54,6,7,89))


# def add(**x):
#   return x["a"] + x["b"];
#
# print(a=10,b=20)

# strs = "he llo worlds"
#
# print(strs.split(" "))
#
# x = [1,2,1.23,4,True, "stas"]
# y = list({1,2,33,False})
# y.append("string")
# print(y)


# x = lambda i,j : print(i+j)
#
#
# x(10,20)


# str="abcd123"
#
# print("Alphabets:",alphabets)
# print("Numbers:",numbers)