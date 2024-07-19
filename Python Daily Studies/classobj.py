#
# class add:
#     def __init__(self,num1,num2,value=0):
#         self.num1 = num1
#         self.num2 = num2
#         self.value = value
#
#
#     def addition(self):
#         self.value += self.num1 + self.num2
#
#
#     def __str__ (self):
#         return (f"{self.num1}+{self.num2}={self.value}")

#
# class sub:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2

#     def subtraction(self):
#         return self.num1 - self.num2

#     def addition(self):
#         return  self.num1 + self.num2
#
#
# a = int(input("enter the number: "))
# b = int(input("enter the number: "))
#
# sub1 = sub(a,b)
# print(sub1.addition())

# while True:
#
#     options = input("enter the add-1 and sub-2:")
#     if options == "1":
#         Add1 = add(a,b)
#         Add1.addition()
#         print(Add1)
#     elif options == "2":
#         Sub1 = sub(a,b)
#         print(Sub1.subtraction())
#     else:
#         break

# class add:
#     def __init__(self,num1,num2,value=0):
#         self.num1 = num1
#         self.num2 = num2
#         self.value = value
#
#     def addition(self):
#         self.value += self.num1 + self.num2
#         return(self.value)

#     def __str__ (self):
#         return (f"{self.num1}+{self.num2}={self.value}")
#
# Sum = add(22,44)
# Sum.addition()
# print(Sum)



# class sub:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
#
# a = int(input("enter the number: "))
# b = int(input("enter the number: "))
#
# while True:
#
#     options = input("enter the add-1 and sub-2:")
#     if options == "1":
#         Add1 = add(a,b)
#         # Add1.addition()
#         print(Add1.addition())
#     elif options == "2":
#         Sub1 = sub(a,b)
#         print(Sub1.subtraction())
#     else:
#         break





# Inheritance
# Single Inheritance
# class add:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2

#     def addition(self):
#         return self.num1 + self.num2

# class sub(add):
#     # def __init__(self,num1,num2):
#     #     self.num1 = num1
#     #     self.num2 = num2

#     def subtraction(self):
#         return self.num1 - self.num2


# while True:
#     a = int(input("enter the number: "))
#     b = int(input("enter the number2: "))
#     options = input("enter the add-1 and sub-2:")
#     Add1 = sub(a, b)
#     if options == "1":
#         print(Add1.addition())
#     elif options == "2":
#         print(Add1.subtraction())
#     else:
#         break





# Multilevel Inheritance
# class add:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def addition(self):
#         return self.num1 + self.num2


# 









#     # def __init__(self, num1, num2):
#     #     self.num1 = num1
#     #     self.num2 = num2

#     def subtraction(self):
#         return self.num1 - self.num2

# class mul(sub):
#     # def __init__(self, num1, num2):
#     #     self.num1 = num1
#     #     self.num2 = num2

#     def multiplication(self):
#         return self.num1 * self.num2

# class div(mul):
#     def division(self):
#         return self.num2/self.num1


# while True:
#     a = int(input("enter the number: "))
#     b = int(input("enter the number2: "))
#     options = input("enter the add-1  sub-2  mul-3  div-4:")
#     cal = div(a,b)
#     if options == "1":
#         print(cal.addition())
#     elif options == "2":
#         print(cal.subtraction())
#     elif options == "3":
#         print(cal.multiplication())

#     elif options == "4":
#         print(cal.division())
#     else:
#         break



# Multiple Inheritance
#
#
# class myclass:
#
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#
#        return self.num1+self.num2
#
#     def sub(self):
#         return self.num2 - self.num1
#
# obj = myclass(34,43)
# print(obj.add())
# print(obj.sub())


# Contructor
#
# class Bio:
#     def __init__(self,sub1,sub2):
#         self.sub1 = sub1
#         self.sub2 = sub2
#
#     def __str__(self):
#         return (f"{self.sub1} and {self.sub2}")
#
# class comp(Bio):
#     pass

#     def __init__(self,sub1,sub2):
#         self.sub1 = sub1
#         self.sub2 = sub2
#         # Bio.__init__(self,sub1,sub2)
#     def __str__(self):
#         return (f'{self.sub1} and {self.sub2}')
# #
#
# sub = comp("Maths","Physics")
# # sub2 = comp()
# print(sub)

# sub=comp("eng","math")
# print(sub)







