import re
s=input("enter the E-mail: ")
valid="^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
if re.match(valid,s):
    print("True")
else:
    print("false")


