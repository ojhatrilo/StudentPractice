# class add:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def addition(self):
#         return self.num1 + self.num2
#
# class sub:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
# while True:
#     a = int(input("enter the number: "))
#     b = int(input("enter the number2: "))
#     options = input("enter the add-1 and sub-2:")
#     if options == "1":
#         Add1 = add(a,b)
#         print(Add1.addition())
#     elif options == "2":
#         Sub1 = sub(a,b)
#         print(Sub1.subtraction())
#     else:
#         break
#



# Inheritance
# Single Inheritance
# class add:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def addition(self):
#         return self.num1 + self.num2
#
# class sub(add):
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
#
# while True:
#     a = int(input("enter the number: "))
#     b = int(input("enter the number2: "))
#     options = input("enter the add-1 and sub-2:")
#     if options == "1":
#         Add1 = sub(a,b)
#         print(Add1.addition())
#     elif options == "2":
#         Sub1 = sub(a,b)
#         print(Sub1.subtraction())
#     else:
#         break

# Multilevel Inheritance
# class add:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def addition(self):
#         return self.num1 + self.num2
#
#
# class sub(add):
#     # def __init__(self, num1, num2):
#     #     self.num1 = num1
#     #     self.num2 = num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
# class mul(sub):
#     # def __init__(self, num1, num2):
#     #     self.num1 = num1
#     #     self.num2 = num2
#
#     def multiplication(self):
#         return self.num1 * self.num2
#
# class div(mul):
#     def division(self):
#         return self.num2/self.num1
#
#
#
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
# class add:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def addition(self):
#         return self.num1 + self.num2
#
# class sub:
#     # def __init__(self,num1,num2):
#     #     self.num1 = num1
#     #     self.num2 = num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
# class mul:
#     # def __init__(self, num1, num2):
#     #     self.num1 = num1
#     #     self.num2 = num2
#
#     def multiplication(self):
#         return self.num1 * self.num2
#
#
# class div:
#     def division(self):
#         return self.num2/self.num1
#
#
#
# class Calculator(add,sub,mul,div):
#     pass
#
# while True:
#     a = int(input("enter the number: "))
#     b = int(input("enter the number2: "))
#     options = input("enter the add-1  sub-2  mul-3  div-4:")
#     cal = Calculator(a,b)
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

# divchange  = div()
# divchange.num2 = 24
# divchange.num1 = 2
# print(divchange.division())








