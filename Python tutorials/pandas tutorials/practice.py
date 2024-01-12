first = 0
second = 1
# print(first)
# print(second)
for x in range(1,7):
    third = first + second
   
    first,second=second,third
print(third)
    
    