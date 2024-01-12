a="i can't cause "
b='use i dumb'
x=a.split()
y=b.split()
z=[]
for i in range(min(len(x),len(y))):
    z.append(x[i])
    z.append(y[i])

s=' '.join(z)
print(s)
print(z)


