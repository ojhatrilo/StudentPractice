input=open('myfile.txt', 'r')
output=open('demo.txt', 'w')



for i in input:
    if i not in output:
        output.write(i)
               
input.close()
output.close()
# text=f.read()

# text1=list(text)
# x=[]
# for i in text1:
#     if x not in i:
#         x.append(i)
        
# print(x)
# f.close()