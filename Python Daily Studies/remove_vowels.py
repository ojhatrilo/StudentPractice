def vowels():
    print("Removing vowels letters from the given word")
    var=input("enter the word:").lower()
    list1=["a","e","i","o","u"]
    end=''
    for i in var:
        if i not in list1:
            end+=''.join(i)
    print(end)

vowels()

# def idmatrix(num):
#     for i in range(num):
#         for j in range(num):
#             if i==j:
#                 print(num,end=" ")
#             else:
#                 print("*",end=" ")
#         print()
