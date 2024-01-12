n=input()
output=''
for i in n:
    if i.isalpha():
        ch=i                
    else:
        d=int(i)
        output=output+d*ch
print(output)
       
      