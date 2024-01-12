a=input()
b=input()
a.split()
b.split()
x=[]
for i in range(min(len(a),len(b))):
    x.append(a[i])
    x.append(b[i])

print(x)
    

