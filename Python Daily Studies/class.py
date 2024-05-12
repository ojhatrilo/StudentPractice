# Creating class and object
# Program to demonstrate 'Variable
# defined outside the class'

# class Hello:
#     x = "Hello iam Executed"
#     print(x)
#
#     def hi(self):
#         return ("Hi")
#
#     def hello(self):
#         return ("ajay")
#
# obj = Hello()
# print(obj.hello())
# print(obj.hi())



class print_str:


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name},{self.age}")

#     def __init__(ke,name,age):
#         ke.name = name
#         ke.age = age
#         # print(ke.name,ke.age)
#
#     def __str__(ke):
#         return (f"{ke.name},{ke.age}")

#
#
hi=print_str("sony",24)
print(hi)



# Python program to illustrate destructor
# class Employee:
#
# 	# Initializing
# 	def __init__(self):
# 		print('Employee created.')
#
# 	# Deleting (Calling destructor)
# 	def __del__(self):
# 		print('Destructor called, Employee deleted.')
#
# obj = Employee()
# del obj



# Variable defined outside the class.
# outVar = 'outside_class'
# print("Outside_class1", outVar)
#
# ''' Class one '''
# class Geek:
# 	print("Outside_class2", outVar)
#
# 	def access_method(self):
# 		print("Outside_class3", outVar)
#
# # Calling method by creating object
# uac = Geek()
# uac.access_method()
#
# ''' Class two '''
# class Another_Geek_class:
# 	print("Outside_class4", outVar)
#
# 	def another_access_method(self):
# 		print("Outside_class5", outVar)
#
# # Calling method by creating object
# uaac = Another_Geek_class()
# uaac.another_access_method()


# class details:
#
# 	def __init__(self):
# 		self.name = "Ranjani"
# 		self.age = 23

# 	def __str__(self):
# 		return (f"name = {self.name}\nAge ={self.age}")
# per = details()
#
# print(per)



# Python program to demonstrate
# single inheritance

# Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")
#
# # Derived class
#
#
# class Child(Parent):
# 	def func2(self):
# 		print("This function is in child class.")
#
#
# # Driver's code
# object = Child()
# object.func1()
# object.func2()
# #
# #
#
# # Python program to demonstrate
# # multiple inheritance
#
# # Base class1
# class Mother:
# 	mothername = ""
#
# 	def mother(self):
# 		print(self.mothername)
#
# # Base class2
#
#
# class Father:
# 	fathername = ""
#
# 	def father(self):
# 		print(self.fathername)
#
# # Derived class
#
#
# class Son(Mother, Father):
# 	def parents(self):
# 		print("Father :", self.fathername)
# 		print("Mother :", self.mothername)
#
#
# # Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()
#
#
#
# # Python program to demonstrate
# # multilevel inheritance
#
# # Base class
#
#
# class Grandfather:
#
# 	def __init__(self, grandfathername):
# 		self.grandfathername = grandfathername
#
# # Intermediate class
#
#
# class Father(Grandfather):
# 	def __init__(self, fathername, grandfathername):
# 		self.fathername = fathername
#
# 		# invoking constructor of Grandfather class
# 		Grandfather.__init__(self, grandfathername)
#
# # Derived class
#
#
# class Son(Father):
# 	def __init__(self, sonname, fathername, grandfathername):
# 		self.sonname = sonname
#
# 		# invoking constructor of Father class
# 		Father.__init__(self, fathername, grandfathername)
#
# 	def print_name(self):
# 		print('Grandfather name :', self.grandfathername)
# 		print("Father name :", self.fathername)
# 		print("Son name :", self.sonname)
#
#
# # Driver code
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()
#

# # Python program to demonstrate
# # Hierarchical inheritance
#
#
# # Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")
#
# # Derived class1
#
#
# class Child1(Parent):
# 	def func2(self):
# 		print("This function is in child 1.")
#
# # Derivied class2
#
#
# class Child2(Parent):
# 	def func3(self):
# 		print("This function is in child 2.")
#
#
# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
#
#
#
#
# # Python program to demonstrate
# # hybrid inheritance
#

# class School:
# 	def func1(self):
# 		print("This function is in school.")
#
#
# class Student1(School):
# 	def func2(self):
# 		print("This function is in student 1. ")
#
#
# class Student2(School):
# 	def func3(self):
# 		print("This function is in student 2.")
#
#
# class Student3(Student1, School):
# 	def func4(self):
# 		print("This function is in student 3.")
#
#
# # Driver's code
# object = Student3()
# object1 = Student2()
# object1.func1()
# # object1.func2()
# object1.func3()



# class Elakkiya:
#     print("XXYY")
#
#     def __init__(self):
#         self.staf1 = "Kishore"
#         self.staf2 = "Karthick"
#         self.staf3 =  "Priya"
#         print(self.staf1+"\n"+self.staf2)
#
# Elakkiya()













