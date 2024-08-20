# Python program to
# demonstrate protected members

# Creating a base class
# class organ:

#     def __init__(self):
#         self._a = 33
#         print(self._a)
		

# class Base:
# 	def __init__(self):

# 		# Protected member
# 		self._ab = 2
# 		print(self._ab)

# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):

# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
# 		print("Calling protected member of base class: ",
# 			self._ab)

# 		# Modify the protected variable:
# 		self._ab = 3
# 		print("Calling modified protected member outside class: ",
# 			self._ab)



# ooj = organ()
# ooj= 44
# ooj = organ()

# obj1 = Derived()
# obj1.ab = 5
# print(obj1.ab)

# obj2 = Base()



# #Calling protected member
# #Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)

# obj1._a = 23

# print("Accessing protected member of obj1: ", obj1._a)

# # #Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)



# Python program to
# demonstrate private members

# Creating a Base class

#
# class Base:
# 	def __init__(self):
# 		self._a = "GeeksforGeeks"
# 		self.__c = "GeeksforGeeks2"

# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):

# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
# 		print("Calling private member of base class: ")
# 		print(self.__c)


# Driver code
# obj1 = Base()
# obj2 = Derived()
# print(obj2._a)
# print(obj2.__c)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class

