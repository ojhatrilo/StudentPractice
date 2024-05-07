# Conditional Statements
# "if" is the keyword used to define the condition
# "else" is the keyword which doesn't satisfies the if condition the else code is executed
# "elif" is the keword to declare multiple conditions for fast excution
# Nested if else is the condition which is return inside the if statemet


# if & else statement example
# a = 23
# b = 34
# if a > b :
#     print('good')
# else:
#     print('bad')

# if, else, elif statement example
# a = int(input("enter the num1:"))

# if a%2==0:
#     print("divisible by 2")
# elif a%3 == 0:
#     print("divisible by 3")
# elif a%4 == 0:
#     print("divisible by 4")
# else:
#     print("invalid input")

# nested if else statement
# a = int(input("enter the num1:"))
# if a>0:
#     if a%2==0:
#         print("divisible by 2")
#     elif a%3 == 0:
#         print("divisible by 3")
#     elif a%4 == 0:
#         print("divisible by 4")
#     else:
#         print("not Match")
#
# else:
#     print("invalid input")
#

num = int(input("Enter the number:"))
# #
if 0<num<100:
    if num > 90:
        print("Grade O")
    elif num > 80:
        print("Grade A")
    elif num > 70:
        print("Grade B")
    elif num > 60:
        print("Grade C")
    elif num >50:
        print("Grade D")
    else:
        print("You are Fail")

else:
    print("Invalid Input")


# num = int(input("Enter the number:"))
#
# if num%2 ==0 or num%3 ==0 or num%5 == 0:
#     print("Not a prime")
# else:
#     print("Is a Prime")





































