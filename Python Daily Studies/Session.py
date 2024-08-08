# num = int(input("enter the number:"))
# num1 = int(input("enter the number2:"))
# sum = num+num1
# print(sum)

# num = str(input("enter the number:"))
# num1 = str(input("enter the number2:"))
# sum = num+num1
# print(sum)

# a = "23"
# g = int(a)
# con_str=str(g)
# con_flo=float(con_str)
#
# print(type(con_flo))

# a = (2,3,4,56)
# print(type(a))
# list1 = tuple(a)
# print(type(list1))

# list1 = [22,33,556,66]
# for i in list1:
#     print(i)





# a = 5
# a+=5
# print(a)

# a = 5
# if a % 2 == 0:
#     print(a)
#     if a%4 == 0:
#         a+=7
#         a+=21
#         a+=34
#         print(a)
#
# elif (a % 5 == 0):
#
#     a+=7
#     a+=21
#     a+=34
#     print(a)
# else:
#     a+=7
#     print(a)

# a = 23
# # print(type(a))
# cov_str = float(a)
# print(type(cov_str))


# Base = 24
# Height = 30
# Area = 1/2*Base*Height
# print(Area)

# a = "Navenna"
# y = slice(0,7,-1)
# print(a[y])
# print(a)

# a = "23"
# b = 23
# c = int(a)+b
# print(c)

# list1 = ["hello",1,"hi",2]
# word = []
# num = []
# for i in list1:
#     if type(i) == str:
#         word.append(i)
#     else:
#         num.append(i)
#
# print(word)
# print(num)


# [1 0 0
#  0 1 0
#  0 0 1 ]

#
# a = input("").split()
# ch = 1
# for i in a:
#     ch*=int(i)
#
# print(ch)



# i = 0
# while i<5:
#     print(i)
#     i+=1
#     while i<4:
#         print(i)
#         i+=1




# list1 = [22,33,45]
# i=0
# while i<len(list1):
#     pass
#     break

# for j in list1:
#     pass
#
# print(list1)













# a = "hi my name is yogesh"
#
# output = "himy nameis YOGESH"
#
#
# b = "hi my name is yogesh"
#
# output1 = "hi my name is Hsegoy"






# class Bank:
#     def __init__(self,balance=0.0) -> None:
#         self.balance = balance

#     def get_balance(self):
#         value = self.balance
#         print(value)

# obj = Bank()
# obj.get_balance()
        
# radius = 1.1
# pi = 3.14
# area = pi * radius ** 2
# print(area)

# formula for area of a triangle is (1/2*base*height)
# base = 5
# height = 2
# area_triangle = 1/2*base*height
# print(area_triangle)



# num1 = str(input("enter number:"))
# num2 = str(input("enter the number:"))


# minimum = int(num1)-int(num2)
# print(minimum)



# firstname = str(input("Enter your name:"))
# lastname = str(input("Enter your lname:"))
# fullname = firstname+" "+lastname
# print(fullname)

# decimal = float(input("Enter your decimal value:"))
# print(decimal)

# num1 = int(input("enter the value:"))
# print(num1)

# a = 23.0
# print(type(a))

# a = "23"
# b = float(a)
# print(b)
# print(type(b))





# a = "Saroj Kumar"

# b = a[0:5]
# reverse = b[::-1]
# print(reverse)


# a = "hi my name is ojha"
# output = "hi my eman is ojha"


# b = "hi iam fine"
# output2 = "fine iam hi"

# # Get the name number form the user 
# # then reverse the number
# sample_input = 5438
# sample_output = 8345


# input = "hi iam the pro coder"
# output ="hi pro coder"


# input1 = "HI MY NAME OJHA"
# output1 = "hi my name ojha"

# input2 = "hi my name is ojha"
# output2 = "himynameis OJHA"

# input3 = ["hello", "Everyone"]
# output3 = ["HELLO", "EVERYONE"]


# question = "hi my name is ojha"
# to_be_reversed = question[6:10]
# reverse = to_be_reversed[::-1]
# replace_1 = question.replace("name",reverse)
# print(replace_1)



# question2 = "hi iam fine"
# reverse_value = question2.split()
# reverse_value.reverse()
# replace_2 = " ".join(reverse_value)
# print(replace_2)


# question3 = 5438
# reverse_value = str(question3)
# reverse_value = reverse_value[::-1]
# num = int(reverse_value)
# print(num)
# print(type(num))

# question4 = "hi iam the pro coder"
# z = question4.replace("iam the",'')
# print(z)

# question5 = "HI MY NAME OJHA"
# question5 = question5.lower()
# print(question5)

# quetion6 ="hi my name is ojha"
# list1 = quetion6.split()
# want_to_be_removed = list1[0:4]
# x = "".join(want_to_be_removed)
# replace = quetion6.replace("hi my name is",x)
# print(replace)

# question7 = ["hello", "Everyone"]
# question7[0] = question7[0].upper()
# question7[1] = question7[1].upper()
# print(question7)

# question7 = ["hello", "Everyone"]
# upp = " ".join(question7).upper()
# x =upp.split()
# print(x)




# a = (22,34,56)
# # a[1] = 45
# z = list(a)
# z[-1] = 99
# x = tuple(z)
# print(x)


# a.append([87,44,78,90])
# print(a)
# print(len(a))


# b = [87,44,78,90]
# a.extend(b)
# print(a)
# print(len(a))


# a = [1,3,4,5,67]
# a.reverse()
# print(a)

# a = 23
# b = float(a)
# print(type(b))



# try:
#     a = int(input("Enter the number:"))
#     b = int(input("Enter the number:"))
#     print(a/b)
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Division error")


# try:
#     a = int(input("Enter the number;"))
#     b = int(input("Enter the number:"))
#     z = a+b

# except ValueError:
#     print("invalid input")

# else:
#     print(z)

# finally:
#     print("mvyg")



# set1 = {25,45,92}
# print(set1)

# a = "hello"
# a.sort()
# print(a)

# a = ["hello","everyone","hi"]
# a[1] = a[1].upper()
# print(a)

# word = a[1]
# z = word.upper()
# a[1] = z
# print(a)


# a = 25
# b = 39

# if a>b:
#     print("a is greater")
# elif a<b:
#     print("b is greater")
# else:
#     print("None of the condition satisfied")

# if a%5 == 0:
#     if b%5 == 0:
#         print("both are divisible by 5")
#     else:
#         print("a is divisible by 5")
# else:
#     print('It is not divisible by 5')



# a = 41
# b = 43

# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")


# if a>b:
#     print("a is greater")
# elif b>a:
#     print("b is greater")
# else:
#     print("both are not satisfied")


# a = 45
# if a%5 == 0 :
#     if a>33:
#         print("a is greater according secerete condition")
#     else:
#         print("a is not greater according secerete condition")
# else:
#     print("a is not divisible by 5")

# a = "hi my name is ojha"
# output = "hi my eman is ojha"

# question = "hi my name is ojha"

# required = a[6:10]
# # print(required)
# reversed = required[::-1]
# ans = question.replace("name",reversed)
# print(ans)




# a = 23.56
# print(type(a))


# print(5%2)




# a = [22,43,56,78]
# for i in a:
#     print(i)



# intro = {
#     "name":"ojha",
#     "age":23,
#     "city":"delhi"
# }
# for i in intro:
# 
#    print(intro[i])
# num1 = str(input("Enter number:"))
# print("hi")
# num2 = str(input("Enter number:"))

# print(type(num1))

# name = input("Enter your name:")
# print(type(name))

# a = '23'
# a = int(a)
# print(a)




# list1=[22,45,85,58,33]
# min=list1[0]
# for i in list1:
#     if i<min:
#         min=i
# print(min) 


# list1=[22,45,85,58,33]
# max=list1[0]
# for i in list1:
#     if i>max:
#         max=i
# print(max)  

# Write a function named capital_indexes. The function takes a single parameter, which is a string.
#  Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

# def capital_indexes(a):
#     list1 = []
#     for i in range(len(a)):
#         if a[i].isupper():
#             list1.append(i)
#     return list1

# output = capital_indexes("HeLlO")
# print(output)

        

# i = 0
# while i<5:
#     print(i)
#     i+=1



'''

1 0 0 
0 1 0
0 0 1

'''
# def identity(num):
#     for i in range(num):
#         for j in range(num):
#             if i == j:
#                 print(1,end=" ")
#             else:
#                 print(0,end=" ")
#         print()


# num = int(input("Enter the number:"))
# identity(num)



# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def add(self):
#         return self.num1 + self.num2
    
#     def sub(self):
#         return self.num1 - self.num2
    
#     def mul(self):
#         return self.num1 * self.num2
    
#     def div(self):
#         return self.num1 / self.num2
    
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# while True:
#     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
#     choice =input("Enter your choice:")
#     obj = Calculator(num1,num2)
#     if choice == "1":
#         print("Addition is:",obj.add())
#     elif choice == "2":
#         print("Subtraction is:",obj.sub())
#     elif choice == "3":1,
#         print("Multiplication is:",obj.mul())
#     elif choice == "4":
#         print("Division is:",obj.div())
#     else:
#         print("Invalid choice")
#         print("Do you want to continue? (y/n):")
#         choice = input()
#         if choice == "y":
#             continue
#         else:
#             break

# def add(num1,num2):
#     return num1 + num2

# def sub (num1,num2) :   
#     return num1 - num2

# def mul (num1,num2) :
#     return num1 * num2
# def div (num1,num2):
#     return num1 / num2

# num1 =int(input ("Enter the first number:"))
# num2 = int(input ("Enter the second number:"))
# while True:
#     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
#     choice = input("Enter your choice:")
#     if choice == "1":
#         print("Addition is:",add(num1,num2))
#     elif choice == "2":
#         print("Subtraction is:",sub(num1,num2))
#     elif choice == "3":
#         print("Multiplication is:",mul(num1,num2))
#     elif choice == "4":
#         print("Division is:",div(num1,num2))
#     else:
#         print("Invalid choice")
#         print("Do you want to continue? (y/n):")
#         choice = input()
#         if choice == "y":
#             continue
#         else:
#             break
        

# list1 = ["hello","god"]
# a= list1[1]
# b=a[0].upper()
# print(b)


# pin = 1234
# amount = 0

# def deposite(value):
#     global amount
#     amount +=value
#     print("Your current balance is:",amount)

# def withdraw(value):
#     global amount
#     if amount < value:
#         print("Insufficient balance")
#     else:
#         amount -=value
#         print("Your current balance is:",amount)

# def balance():
#     global amount
#     print("Your current balance is:",amount)

# def user_pin(value):
#     global pin
#     if value == pin:
#         new_pin = int(input("Enter your new pin"))
#         pin = new_pin
#     else:
#         print("invalid pin")

    
# while True:
#     cus_pin = int(input("Enter the pin number:"))
#     if cus_pin == pin:
#         print("Welcome to our account")
#         user_pin(cus_pin)    
#         print("1.Deposite\n2.Withdraw\n3.Balance\n4.Exit")
#         choice = input("Enter your choice:")
#         if choice == "1":
#             value1 = int(input("Enter the amount:"))
#             deposite(value1)
#         elif choice == "2":
#             value2 = int(input("Enter the amount:"))
#             withdraw(value2)
#         elif choice == "3":
#             balance()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice")
#     else:
#         print("invalid Pin")

# class add:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __str__ (self):
#         # return (f"Addition of {self.a} and {self.b} is {self.a+self.b}")
#         return str(self.a)
    

# obj = add(56,23)
# print(obj)

# class Add:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def addition(self):
#         return self.a + self.b
    
# class Sub:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def subtraction(self):
#         return self.a - self.b
    
# class Mul:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def multiplication(self):
#         return self.a * self.b
    
# class Div:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def divide(self):
#         return self.a / self.b


# class Calculator(Add,Sub,Mul,Div):
#     pass

# obj = Calculator(4,2)
# print(obj.addition())


# a = 56
# b = 47

# if a<b:
#     if b>a:
#         print("b is greater than a")
#     else:
#         print("a is greater than b")
# else:
#     print("a is greater than b")


# Reverse the nuber


# age = 23
# name = "adline"

# print(f"{name} {name} {age} {age}")

# try:
#     a = int(input("Enter the first number:"))
#     b = int(input("Enter the second number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Wrong input for division")
# except ValueError:
#     print("Entered value dosen't mathch with the datatype")
# finally:
#     print("Have a Good Day")



# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# print(a/b)

# a = "hi iam fine"
# x = a.split()
# x.reverse()
# print(x)
# y = " ".join(x)
# print(y)


# a = "hi iam fine"
# x = a[0:2]
# y = a[3:6]
# z = a[7:]
# print(z,y,x)
# z = a[::-1]
# print(z)


# a = 5854
# x = a[-1]
# print(x)



# a = 45
# b = 56
# if a>b:
#     a +=30
#     print("a is greater than b")
#     print(a)
# if a == b:
#     print("a is equal to b")

# else:
#     b +=30
#     print("b is greater than a")
#     print(b)


# a = ["Welcome to python programing Language"]
# x = a[0].split()
# x[2] = x[2].upper()
# z = " ".join(x)
# a[0] = z
# print(a)


# try:
#     a = int(input("enter the number:"))
#     if a % 2 == 0:
#         print("even number")
#     else:
#         print("odd number")
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Zero division error")


# a = int(input("enter the number:"))
# print(a)

# print("Finally i have got executed")

# list1 = [68,47,34,44,92]
# # print(list1[0])
# # print(list1[1])
# # print(list1[2])
# # print(list1[3])
# # print(list1[4])
# for i in list1:
#     print(i)



# list1 = [68,47,34,44,92,1]

# minimum = list1[0]#47 34 1
# for i in list1:
#     if i < minimum:
#         minimum = i
# print(minimum)
        


# a = int(input("enter the number:"))

# if a%2 ==0 and a%3 == 0 :
#     print("number is divisible by 2 and 3")
# elif a%5 == 0 or a%10 == 0:
#     print("number is divisible by 5 or 10")
# else:
#     print("number is not divisible by 2,3,5,10")


# list1 = [23,12,44,"hi",'hello','yellow',30]
# num=[]
# str=[]
# for i in list1:
#     if type(i)==int:
#         num.append(i)
#     else:
#         str.append(i)
# print(num)
# print(str)

# val = int(input("enter the number:"))
# adder = 0
# for c in range(1,val,3):
#     adder += c
#     if c%2 == 0 :
#         print(c*10)
#     else:
#         print(adder)

# print(c)



# a = "iam good not"
# b = "you are super"

# list1 = a.split()
# list2 = b.split()

# output = []

# for i in range(len(list1)):
#     output.append(list1[i])
#     output.append(list2[i])

# str1 = ' '.join(output)
# print(str1)


# a = [56,56,23,44,44,29]

# list1 = [4,1,1,4,1,1,1]

# for i in list1:
#     print('* '*i)

# n = int(input("Enter the Number:"))
# for i in range(1,n):
#     print(" "*(n-i-1),"* "*i)

  # Output: 64


# avg function
# min function
# max function
# sort function

# Python program for implementation of Selection
# Sort
# A = [64, 25, 12, 22, 11]

# Traverse through all array elements
# for i in range(len(A)-1):
    
#     # Find the minimum element in remaining 
#     # unsorted array
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
            
#     # Swap the found minimum element with 
#     # the first element        
#     A[i], A[min_idx] = A[min_idx], A[i]

# # Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#     print(A[i],end=" ") 


# a = 23
# def change():
#   global a
#   a = 40

# change()
# print(a)  # Output: 23

# students = [
#     {'name': 'Priya','age': 99, 'rank': 5},
#     {'name': 'Amma', 'age': 45, 'rank': 100},
#     {'name': 'Arun', 'age': 29, 'rank': 2},
#     {'name': 'Ranju','age': 94, 'rank': 4},
#     {'name': 'Appa', 'age': 52, 'rank': 99}
# ]

# def min_rank(data):
#   rank = data[0]['rank']
#   count = 0
#   for i in range(len(students)):  
#     if rank>data[i]['rank']:
#       rank = data[i]['rank']
#       count = i
#   return data[count]

# print(min_rank(students))    
# print(students[2]['rank'])

# def add(a,b):
#     return a+b

# print(add(6,3))

# x = lambda a,b : a+b
# print(x(5,7))  # Output: 12

# def add(n):
#     return n + n

# list1 = [25,23,56,5]

# x = map(add,list1)
# print(list(x))  # Output: [50, 46, 112, 10]


# list1 = [54,30,20,40]
# min = list1[0]
# for i in list1:
#     if i<min:
#         min = i 

# print(min)

# for i in range(0,4):
#     for j in range(0,4):
#         print(i,j)


# i = 0
# while i < 5:
#     print(i)
#     i+=1  


# def hi():
#     print("Hello, World!")
# hi()

# 


# list1 = [25,34,56,72]
# def hi(we):
#     for i in we:
#         yield i

# print(list(hi(list1)))
    


# class Helllo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print("Hello, my name is", self.name, "and I am", self.age)

#     def hi(self,a):
#         print (self.name, a)
      
    # def __str__(k) -> str:
    #     return (f"Hello, my name is {k.name} and I am {k.age}")
      
    

# obj = Helllo('Mahima',23)
# obj.display()
# obj.hi(56)


# def add(a,b):
#     return a+b
# print(add(5,7))