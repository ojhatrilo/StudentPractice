numbers=[1,2,3,4,5,6,7,8,9]
x=[]
y=[]
z=[]
for i in range(0,len(numbers),2):
    value=numbers[i]
    x.append(value)
x.sort()
x.reverse()
print(x)
for j in range(1,len(numbers),2):
    value2=numbers[j]
    y.append(value2)
y.sort()
print(y)    
for l in range(min(len(x),len(y))):
    z.append(x[l])
    z.append(y[l])
    
    
print(z)
    

       