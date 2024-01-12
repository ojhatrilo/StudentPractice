array1=[2,4,5,6,7,8,9,21]
array2=[2,3,4,5,6,7,8,9,11,15]
array3=[]
array1.extend(array2)

x=array1
print(x)
for i in x:
    if i not in array3:
        array3.append(i)
    
print(array3)
