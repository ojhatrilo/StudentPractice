class add:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

class sub:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def subtraction(self):
        return self.num1 - self.num2

while True:
    a = int(input("enter the number: "))
    b = int(input("enter the number2: "))
    options = input("enter the add-1 and sub-2:")
    if options == "1":
        Add1 = add(a,b)
        print(Add1.addition())
    elif options == "2":
        Sub1 = sub(a,b)
        print(Sub1.subtraction())
    else:
        break







