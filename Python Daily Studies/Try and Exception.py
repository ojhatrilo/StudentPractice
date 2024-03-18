try:
    def hello():
        try:
            a = int(input("Enter the number;"))
            b = int(input("Enter the number:"))
            z = a+b

        except ValueError:
            print("invalid")

        else:
            print(z)

    hello()
except NameError:
    print("error")



