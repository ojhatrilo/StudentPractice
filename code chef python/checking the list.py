def same(a,b):
    first_num=a[0]
    last_num=b[-1]
    if first_num==last_num:
        return True
    else:
        return False
    
num_y=[4,3,2,1]   
num_x=[1,2,3,4]
print(same(num_x, num_y))

