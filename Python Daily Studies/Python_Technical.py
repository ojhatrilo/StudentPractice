# # PassWord Validtion

# Password = input("Enter your Password:")
# Password_len = len(Password)

# upper_avl,lower_avl,special_char,num_avl,no_space = False,False,False,False,False

# if Password_len >=8 and Password_len < 20:
#     for i in Password:
#         if i.isupper():
#             upper_avl = True
#         if i.islower():
#             lower_avl = True
#         special = ["@","_","$","*","."]
#         if i in special:
#             special_char = True
#         if i.isdigit():
#             num_avl = True
#         if i != " ":
#             no_space = True

# print({
#     "uppercase":upper_avl,
#     "lowercase":lower_avl,
#     "special_char":special_char,
#     "number":num_avl,
#     "no_space":no_space
# })


# # Count the occurence of the string

# s1 = "India is beautiful country"
# values = {}
# for i in s1:
#     if i not in values:
#         values[i] = 1
#     else:
#         values[i] += 1
# print(values)