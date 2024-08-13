# Python program to
# demonstrate protected members

# Creating a base class
# class Base:
# 	def __init__(self):

# 		# Protected member
# 		self._a = 2
 
# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):

# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
# 		print("Calling protected member of base class: ",
# 			self._a)

# 		# Modify the protected variable:
# 		self._a = 3
# 		print("Calling modified protected member outside class: ",
# 			self._a)


#
# obj1 = Derived()

# obj2 = Base()
# obj2._a = 45
# print(obj2._a)
# #
# # Calling protected member
# # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
#
# # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)




# Python program to
# demonstrate private members

# Creating a Base class


# class Base:
# 	def __init__(self):
# 		self.a = "GeeksforGeeks"
# 		self.__c = "GeeksforGeeks1"

# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):

# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
# 		print("Calling private member of base class: ")
# 		print(self.a)

# obj1 = Derived()
# Driver code
# obj1 = Base()
# print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class





# program to illustrate protected access modifier in a class

# super class


# class Student:
#
#     # protected data members
#     _name = None
#     _roll = None
#     _branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
#
#     # protected member function
#     def _displayRollAndBranch(self):
#
#         # accessing protected data members
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)
#
#
# # derived class
# class Geek(Student):
#
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)
#
#
#     # public member function
#     def displayDetails(self):
#
#               # accessing protected data members of super class
#         print("Name: ", self._name)
#         # _name = "harish"
#
#         # accessing protected member functions of super class
#         self._displayRollAndBranch()
#
#
# # creating objects of the derived class
# obj = Geek("R2J", 1706256, "Information Technology")
#
# # calling public member functions of the class
#
#
# obj.name = "harish"
# obj.displayDetails()




# program to illustrate access modifiers of a class

# super class


# class Super:
#
#     # public data member
#     var1 = None
#
#     # protected data member
#     _var2 = None
#
#     # private data member
#     __var3 = None
#
#     # constructor
#     def __init__(self, var1, var2, var3):
#         self.var1 = var1
#         self._var2 = var2
#         self.__var3 = var3
#
#   # public member function
#     def displayPublicMembers(self):
#
#         # accessing public data members
#         print("Public Data Member: ", self.var1)
#
#     # protected member function
#     def _displayProtectedMembers(self):
#
#         # accessing protected data members
#         print("Protected Data Member: ", self._var2)
#
#     # private member function
#     def __displayPrivateMembers(self):
#
#         # accessing private data members
#         print("Private Data Member: ", self.__var3)
#
#     # public member function
#     def accessPrivateMembers(self):
#
#         # accessing private member function
#         self.__displayPrivateMembers()

# derived class


# class Sub(Super):
#
#       # constructor
#     def __init__(self, var1, var2, var3):
#         Super.__init__(self, var1, var2, var3)
#
#       # public member function
#     def accessProtectedMembers(self):
#
#         # accessing protected member functions of super class
#         self._displayProtectedMembers()
#
#
# # creating objects of the derived class
# obj = Sub("Geeks", 4, "Geeks !")
#
# # calling public member functions of the class
# obj.displayPublicMembers()
# obj.accessProtectedMembers()
# obj.accessPrivateMembers()
#
# # Object can access protected member
# print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)



# protected
# class admin:
#     def __init__(self):
#         self._name = "Harish"
#
# class dup(admin):#
#     def show(self):
#         self.name = "solo"
#         print(self._name)
#
#
# obj = dup()
# obj.show()


# Private
# class admin:
#     def __init__(self):
#         self.__name = "Harish"
#
# class dup(admin):#
#     def show(self):
#         # self.__name = "solo"
#         print(self.__name)
#
#
# obj = dup()
# obj.show()
















