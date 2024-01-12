# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    
    H=list(map(int,input().split(" ")))
    c=0
    
    for j in range(n):
        if(H[j] > k):
            c+=1
    print(c)