
def idmatrix(num):
    for i in range(num):
        for j in range(num):
            if i==j:
                print(num,end=" ")
            else:
                print("*",end=" ")
        print()



