str1 = "abc"
previous = ""
list1 = []
for i in range(len(str1)):
    for j in range(i,len(str1)):
        list1.append(str1[i:j+1])
print(list1)


