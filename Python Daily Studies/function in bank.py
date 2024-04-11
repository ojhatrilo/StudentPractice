amount  = 0

def withdrawl(user):
    global amount
    if user > amount:
        print("In Sufficient",amount)
    else:
        print(user)
        amount-=user
        print("balance",amount)

def deposite(user):
    global amount
    amount+=user
    print("balance",amount)

def balance():
    global amount
    print("Available",amount)

while(True):
    print('''
            press - 1 to deposite
            press - 2 to withdrawl
            press - 3 to balance
            press - Q to exit
                                      ''')
    options = input("Enter the Option:").upper()
    if options == "1":
        num1 = int(input("enter the nuber:"))
        deposite(num1)
    elif options == "2":
        num1 = int(input("enter the nuber:"))
        withdrawl(num1)
    elif options == "3":
        balance()
    elif options == "Q":
        break