# import package as pk
# from package import add,sub 

# x = dir(pk)
# print(x)

# Add1 = sub(2,3)
# print(Add1.subtraction())

# pk.options()

#

# import package as pk
# options()
# a = pk.person1["age"]
# print(a)
#
# pk.person1['name']='ranjani'
# print(pk.person1)
#
# import sys
#
# sys.path.append("D://StudentPractice//modules_package")
#

# import hello
# hello.hi()

# import identity as iden
#
# iden.idmatrix()


# # import hello
# # hello.hi()
#
# import identity as iden
#
# iden.idmatrix()
#

# print(__name__)

# import Functions as fun
# fun.my_function()


# obj = dir(fun)
# print(obj)

# from function_in_bank import *
# withdrawl()

# import function_in_bank as bk

# bk.withdrawl()





# import package as pk
# pk.options()


# from package import person1

# print(person1.get('name'))



# import package
# print(dir(package))

x=input("Enter first name:")
y=input("Enter second name:")
x=x.replace(" ","")  	
y=y.replace(" ","") 
x=list(x) 
y=list(y)
for i in x[:]:
    if i in y:
        x.remove(i) 
        y.remove(i)
count=len(x)+len(y)
result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] 
while len(result) > 1 : 
	split_index = (count % len(result) - 1) 
	if (split_index>=0) : 
		right = result[split_index + 1 : ]
		left = result[ : split_index] 
		result = right + left
	else : 
		result = result[ : len(result) - 1] 
print(result)


















