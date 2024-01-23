list1 = [19,23,44,88,23,19]
count ={}

for i in list1:
    if i not in count:
        count[i] = 1
    else:
        count[i]+=1

print(count)