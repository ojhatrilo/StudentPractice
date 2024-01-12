t=int(input("enter the number of test cases"))
for i in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    count=0
    for j in range(n):
        if h[j]>k:
            count+=1
print(count)