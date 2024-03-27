
# f = open("demo.txt","w")

# f.write("Hello i have deleted all the above content")
# f.close

# f = open("demo.txt","r")
# print(f.read())

# f = open("demo.txt", "a+")

# f.close() # read

# f = open("demo.txt", "r")
# print(f.read())


input=open('demo.txt', 'r')
output=open('demo2.txt', 'w+')
text=input.read()
z=text.split()
y=[]

for i in z:
    if i not in y:
        y.append(i)

x=" ".join(y)  
output.write(x)
input.close()
output.close()
        