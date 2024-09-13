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


# Code Demo - 1
# Sorted Method
# def are_anagrams(str1, str2):
#     # Your code here
#     if sorted(str1)==sorted(str2):
#         return "Given String is anagram"
#     else:
#         return "Given String is not anagram"

# # Test cases
# print(are_anagrams("listen", "silent"))  # Should return True
# print(are_anagrams("hello", "world"))    # Should return False


# Code Demo - 2 
# def are_anagrams(str1, str2):
#     # Your code here
#     for i in str1:
#         if i not in str2:
#             return "Given String is not a anagram"
#         else:
#             return "Given String is a anagram"


# # Test cases
# print(are_anagrams("listen", "silent"))  # Should return True
# print(are_anagrams("hello", "world"))    # Should return False


# def longest_unique_substring(s):
#     start = 0
#     max_length = 0
#     max_substring = ""
#     char_index_map = {}

#     for end in range(len(s)):
#         if s[end] in char_index_map:
#             start = max(start, char_index_map[s[end]] + 1)
#         char_index_map[s[end]] = end
#         if end - start + 1 > max_length:
#             max_length = end - start + 1
#             max_substring = s[start:end + 1]

#     return max_substring

# # Test cases
# print(longest_unique_substring("abcabcbb"))  # Should return "abc"
# print(longest_unique_substring("bbbbb"))     # Should return "b"
# print(longest_unique_substring("pwwkew"))    # Should return "wke"
