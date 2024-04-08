# While loops
# i = 0
# while i<4:
#     print(i)
#     i+=1
#     while i<4:
#         print(i)
#         i+=1

seceret = 7

print("Guess the number Between 1 to 10")

while(True):
    a = int(input("enter the number:"))
    if a == seceret:
        print("you win")
        break
    elif a > seceret:
        print("it is too high")
    elif a < seceret:
        print("too low")
    else:
        print("invalid Input")

# # Break
# i = 0
# while i<4:
#     print(i)
#     continue
#     i += 1


# pass
# for i in range(2):
#     pass


# i = 6
#
# while i>5:
#     print(i)
#     i+=1





# def expand_string(input_str):
#     output = ""
#     i = 0
#     while i < len(input_str):
#         char = input_str[i]
#         if char.isalpha():
#             count = ""
#             i += 1
#             while i < len(input_str) and input_str[i].isdigit():
#                 count += input_str[i]
#                 i += 1
#             count = int(count)
#             output += char * count
#         # else:
#         #     output += char
#         #     i += 1
#     return output
#
# # Test the function
# input_str = "a100b12c111"
# output_str = expand_string(input_str)
# print(output_str)


















