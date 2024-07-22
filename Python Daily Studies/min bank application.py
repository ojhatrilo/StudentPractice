# class Coustomer:
#     bankname="OJHA"
#     def __init__ (self,name,balance=0.0):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("total available balance is:",self.balance)
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("you have insufficient balance")
#         else:
#             self.balance=self.balance-amount
#             print("available balance is: ",self.balance)
            
# print("welcome to",Coustomer.bankname)
# name=input("enter your name")
# data=Coustomer(name)
# while True:    
#     print("w-withdraw\nd-deposite\ne-exit")
#     option=input("enter the operation you want to perform").lower()
#     if option=='d':
#         amount=float(input("enter the amout to be depositted:"))
#         data.deposit(amount)
#     elif option=='w':
#         amount=float(input("enter the amout to be withdraw:"))
#         data.withdraw(amount)
#     elif option=='e':
#         break
#     else:
#         print("the given input doesn't perform operation")
        
        