#
# def addition(num1,num2):
#     return num1+num2
#
# def subtraction(num1,num2):
#     return num1-num2
#
# def multiplication(num1,num2):
#     return num1*num2
#
# def division(num1,num2):
#     return num1/num2
#
#
#
#
#
#
# while(True):
#     print("press 1-add\npress 2-sub\npress 3-mul\npress 4-div\npress q-quit")
#     option = input("Enter the Option:")
#
#     value_1 = int(input("Enter the number:"))
#     value_2 = int(input("Enter the number:"))
#
#     if value_2 > value_1:
#         # temp = value_2
#         # value_2 = value_1
#         # value_1 = temp
#         value_1,value_2 = value_2,value_1
#     else:
#         # temp = value_1
#         # value_1 = value_2
#         # value_2 = temp
#         value_2,value_1 = value_1,value_2
#
#
#     if option == "1":
#        print(addition(value_1,value_2))
#     elif option == "2":
#         print(subtraction(value_1,value_2))
#     elif option == "3":
#         print(multiplication(value_1,value_2))
#     elif option == "4":
#         print(division(value_1,value_2))
#     elif option == "q":
#         break
#     else:
#         print("please enter the valid option")




# Calaculator 2.o

def add(n1, n2):
    return (n1 + n2)


def sub(n1, n2):
    return (n1 - n2)


def mul(n1, n2):
    return (n1 * n2)


def div(n1, n2):
    return (n1 / n2)


def call():
    # while True:
    n1 = int(input("Enter your 1st value: "))
    n2 = int(input("Enter your 2st value: "))

    print("Menu\n"
          "1 for addition\n"
          "2 for substraction\n"
          "3 for multiplication\n"
          "4 for division")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(add(n1, n2))

    elif choice == 2:
        print(sub(n1, n2))

    elif choice == 3:
        print(mul(n1, n2))

    elif choice == 4:
        print(div(n1, n2))

    else:
        print("Invalid choice")


i = 0
while True:
    if i == 0:

        opt = input("enter the option to start. Yes/NO: ")
        i += 1

    else:
        opt = input("Want another calculation? yes/no: ")

    if opt.lower() == "no":
        print("Calculations done")
        break
    elif opt.lower() == "yes":
        # continue
        call()
    else:
        print("Invalid input")
        # break



















