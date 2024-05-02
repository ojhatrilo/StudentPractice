# list1 = [45,32,11,44,50]
# print('maimum value',max(list1))
# print('minimum value',min(list1))
#
# max_value = list1[0]
# min_value = list1[0]
# for i in list1:
#     if i > max_value:
#         max_value = i
#     elif i < min_value:
#         min_value = i

# for i in list1:
#     if i < min_value:
#         min_value = i

# print(max_value)
# print(min_value)

# limit = 5
# user_list = []
# for i in range(limit):
#     x = int(input("enter the element"))
#     user_list.append(x)
# print(user_list)

# a = 'allibaba is bad'
# b = 'cheran is good'
# x = a.split()
# y = b.split()
#
# final = []
# for i in range(min(len(x),len(y))):
#     final.append(x[i])
#     final.append(y[i])
#
# print(final)

# Nested for loop
# for i in range(1,3):
#     for j in range(1,3):
#         print(i,j)


#
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end=' ')
#     print()


# list1 = ["tea","eat","ate","act","cat","tac"]
# group1 = list1[0]
# group = []
# group2 =[]
#
# for i in list1:
#     if sorted(group1) == sorted(i):
#         group.append(i)
#     else:
#         group2.append(i)
#
# print(group)
# print(group2)


# input_str = "aaaccvv"
#
# prev = input_str[0]
# output = ""
# count = 0
# for i in input_str:
#     if i == prev:
#         count +=1
#     else:
#         output += prev+str(count)
#         count = 1
#         prev = i
# output += prev+str(count)
# print(output)


# a = "iam good"
# b = "he is is great"
#
# sep1 = a.split()
# sep2 = b.split()
#
# output = []
#
# x = len(sep1) # 2
# y = len(sep2)  # 4
#
# if x>y:
#     more = x
#     high = sep1
# else:
#     more = y
#     high = sep2
#
# if y<x:
#      less = y
# else:
#     less = x
#
#
# for i in range(min(len(sep1),len(sep2))):
#     output.append(sep1[i])
#     output.append(sep2[i])
#
# for j in range(less,more):
#     output.append(high[j])
#
# print(output)
# #



# for i in range(1,3):
#     for j in range(1,3):
#         for k in range(1,3):
#             print(i,j,k)










#
# seceret = 10
#
#
# for i in range(3):
#     user = int(input("enter the number:"))
#     if user == seceret:
#         print("win")
#         break
#     else:
#         print("you loose continue")
#         break

#
# list1 = [22,44,55,44,55,22]
#
# count = 0
# value = list1[0]
# list2 = []
#
# for i in list1:
#     value = i
#     for j in list1:
#         if i == j:
#             count +=1
#
#     if (str(i)+"-"+str(count)) not in list2:
#         list2.append(str(i)+"-"+str(count))
#         count = 0
#     else:
#         count = 0
#
#
# print(list2)


# def group_anagrams(words):
#     anagram_dict = {}
#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#         else:
#             anagram_dict[sorted_word] = [word]
#     return list(anagram_dict.values())
#
#
# words = ['lump', 'eat', 'me', 'tea', 'em', 'plum']
# print(group_anagrams(words))



# list1 = [56,23,15,45,34,72]
#
# for num in list1:
#     if num%2 != 0:
#         print(num)


# n = int(input("Enter The number:"))
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print("*",end=" ")
#         else:
#             print(0,end=" ")
#     print()


# n = int(input("enter the number:"))
# for i in range(1,n):
#     print(" "*(n-i-1),"* "*i)

#
# a = [22,33,45,67]
#
# for i in a:
#     print(i+5)

# a = [22,33,45,67]
# for i in range(0,3):
#     print(i)


# for i in range(0,3):
#     for j in range(0,3):
#         print(i,j)
























