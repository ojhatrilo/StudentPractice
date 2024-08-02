# amount  = 0

# def withdrawl(user):
#     global amount
#     if user > amount:
#         print("In Sufficient",amount)
#     else:
#         print(user)
#         amount-=user
#         print("balance",amount)

# def deposite(user):
#     global amount
#     amount+=user
#     print("balance",amount)

# def balance():
#     global amount
#     print("Available",amount)



# while(True):
#     print('''
#             press - 1 to deposite
#             press - 2 to withdrawl
#             press - 3 to balance
#             press - Q to exit
#                                       ''')
#     options = input("Enter the Option:").upper()
#     if options == "1":
#         num1 = int(input("enter the nuber:"))
#         deposite(num1)
#     elif options == "2":
#         num1 = int(input("enter the nuber:"))
#         withdrawl(num1)
#     elif options == "3":
#         balance()
#     elif options == "Q":
#         break

# user_pin = 1234
# amount = 0

# print("Welcome")


# def deposit(money):
#     global amount
#     amount += money
#     print("current balance", amount)


# def withdraw(money):
#     global amount
#     if money > amount:
#         print("In sufficiant balance, please try again!!")
#     else:
#         print(money)
#         amount -= money
#         print("After withdraw balance: ", amount)


# def pin_change(pin):
#     global user_pin
#     if len(str(pin))==4:
#         user_pin = pin
#         print ("Pin changed successfully completed")
#         print("your new pin is: ", user_pin)
#         return True
#     else:
#         print("The format is invalid")
#         pin_validate()

# def pin_validate():

#     while True:
#         new_pin = int(input("Enter your new pin: "))
#         cor =pin_change(new_pin)
#         if cor == True:
#             break


# def atm():
#     pin = int(input("\nEnter your 4 digit PIN: "))

#     if user_pin == pin:
#         print("\nWelcome to your account")

#         while True:

#             print("\nEnter your mode of action:\n"
#                   "press 1 for check balance\n"
#                   "press 2 for deposit\n"
#                   "press 3 withdraw\n"
#                   "press 4 for change PIN\n"
#                   "press 5 for exit\n")

#             action = int(input("Enter your choice: "))

#             if action == 1:
#                 print("Balance in your account is:", amount)
#             elif action == 2:
#                 d_amount = float(input("Enter the amount you want to deposit: "))
#                 deposit(d_amount)
#             elif action == 3:
#                 w_amount = float(input("Enter the amount you want to withdraw: "))
#                 withdraw(w_amount)
#             elif action == 4:
#                 old_pin = int(input("Please enter your old pin: "))
#                 if old_pin == user_pin:
#                     new_pin = int(input("Enter your new pin: "))
#                     pin_change(new_pin)
#                     # new_pin = int(input("Enter your new pin: "))
#                     # pin_change(new_pin)
#                     atm()
#                 else:
#                     print("Please check your old pin.")
#             elif action == 5:
#                 print("Thanks for using,\n"
#                       "visit again.:)")
#                 break
#             else:
#                 print("invalid option,Try again")
#     else:
#         print("Invalid pin!!!\n"
#               "Please check your pin.")

# atm()
