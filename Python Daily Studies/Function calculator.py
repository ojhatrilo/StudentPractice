
def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2





while(True):
    print("press 1-add\npress 2-sub\npress 3-mul\npress 4-div\npress q-quit")
    option = input("Enter the Option:")
    value_1 = int(input("Enter the number:"))
    value_2 = int(input("Enter the number:"))

    # if value_2 > value_1:
    #     # temp = value_2
    #     # value_2 = value_1
    #     # value_1 = temp
    #     value_1,value_2 = value_2,value_1
    # else:
    #     # temp = value_1
    #     # value_1 = value_2
    #     # value_2 = temp
    #     value_2,value_1 = value_1,value_2


    if option == "1":
       print(addition(value_1,value_2))
    elif option == "2":
        print(subtraction(value_1,value_2))
    elif option == "3":
        print(multiplication(value_1,value_2))
    elif option == "4":
        print(division(value_1,value_2))
    elif option == "q":
        break
    else:
        print("please enter the valid option")