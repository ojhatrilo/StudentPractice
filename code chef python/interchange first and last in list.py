list1=[1,2,3,4,5]
if list1[0]<list1[-1]:
    tmp=list1[0]
    list1[0]=list1[-1]
    list1[-1]=tmp
    
    print(list1)
    
