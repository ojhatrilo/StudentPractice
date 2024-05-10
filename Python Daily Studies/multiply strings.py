# list1 = ['apple','banana','grapes',67,78,90]
# word = []
# num = []
#
# for i in list1:
#     if type('e')==type(i):
#         z = i.capitalize()
#         word.append(z)
#     else:
#         num.append(i)
# print(word)
# print(num)
# list1 = ['23','44','56']
# count =0
# for i in list1:
#     count+=1
#
# print(count)
# PALINDROME OR NOT:
# string=input("Enter the string:")
# rev_string=string[::-1]
# if string==rev_string:
#     print("palindrome")
# else:
#     print("not palindrome")
# FIBONACCI SERIES:
b=int(input("Enter the no.of terms:"))
first,second=0,1
print(first)
print(second)
for i in range(1,b):
    third=first
    first=second
    second=third+first
    print(first)




