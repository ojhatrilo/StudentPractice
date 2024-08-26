
# f = open("demo.txt","w")
# f.write("Hello i have deleted all the above content")
# f.close()


# f = open("demo3.txt","a")
# f.write("Hello i have deleted all the above content")
# f.close()


# f = open("demo3.txt", "w")
# f.write("Hello i have deleted all the above content")
# f.close()

# f = open("demo.txt", "a+")
# f.write("\nhello iam elakiya")

# f.close()



# read

# f = open("demo.txt", "r")
# print(f.read())


# input=open('demo.txt', 'r')
# output=open('demo2.txt', 'w+')
# text=input.read()
# z=text.split()
# y=[]

# for i in z:
#     if i not in y:
#         y.append(i)

# x=" ".join(y)
# output.write(x)
# input.close()
# output.close()


# create file

# file = open("myfile.txt",'r')
# output = open("myfile2.txt",'w')
#
# file.write("hi my student is always taking leave for exam \nso i will be teaching new concepts \nwithout going backward")
#
# file.close()
# input = file.read()

# print(input.replace(" ",""))

# z = input.replace(" her","her")
# output.write(z)
# file.close()
# output.close()


# f = open("hello.txt",'x')
# f.write("hello iam mathavan")
# f.close()

# f = open("hello.txt",'r')
# print(f.read())


# import os
# os.remove("myfile2.txt")


# file = open('myfile2.txt','w')
# text = "\nShe is a fantastic, Dashing, and beautifull"
# file.write(text)
# file.close()


file = open("myfile.txt", 'r')
print(file.read())