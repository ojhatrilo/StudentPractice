# class add:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def addition(self):
#         return self.num1 + self.num2

# # if __name__ == '__main__':
# #     add2 = add(5,4)
# #     print(add2.addition())


# class sub(add):
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

# def options():
#     while True:
#         a = int(input("enter the number: "))
#         b = int(input("enter the number2: "))
#         options = input("enter the add-1  sub-2  mul-3  div-4:")
#         cal = div(a,b)
#         if options == "1":
#             print(cal.addition())
#         elif options == "2":
#             print(cal.subtraction())
#         elif options == "3":
#             print(cal.multiplication())
#         elif options == "4":
#             print(cal.division())
#         else:
#             break



# person1 = {
#     'name':'tharani',
#     'age': 24
# }

# list2 = [22,34,56,67,67,34]
# list1 = []
# for i in list2:
#     if i not in list1:
#         list1.append(i)

# print(list1)