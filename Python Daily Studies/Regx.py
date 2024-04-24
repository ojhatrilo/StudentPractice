# []	A set of characters	"[a-m]"
# \	    Signals a special sequence (can also be used to escape special characters)	"\d"
# .	    Any character (except newline character)	"he..o"
# ^	    Starts with	"^hello"
# $	    Ends with	"planet$"
# *	    Zero or more occurrences	"he.*o"
# +	    One or more occurrences	"he.+o"
# ?	    Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	    Either or	"falls|stays"
# ()	Capture and group


import re
# s=input("enter the E-mail: ")
# valid="^[a-z0-9]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
# if re.match(valid,s):
#     print("True")
# else:
#     print("false")


# Validating phone no

# s = input("Enter the phone no")
# valid = "^[0-9]{10}$"
# if re.match(valid,s):
#     print("Valid number")
# else:
#     print("Invalid number")

# Alphanum values

# s = input("Enter the Number:")
# valid = "^[0-9]+[a-z]$"
# if re.match(valid,s):
#     print("Valid")
# else:
#     print("invalid")


# import re
#
# pattern = r'^[a-zA-Z0-9]{8}$'  # This pattern matches strings with exactly 8 alphanumeric characters
# input_str = input("enter the number:")
#
# if re.match(pattern, input_str):
#     print("Valid input")
# else:
#     print("Invalid input")
