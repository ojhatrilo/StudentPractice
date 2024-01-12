t=int(input("enter the number of test cases:"))
ans=''
for i in range(t):
    s=input().lower()#seceret word
    g=input().lower()#gusses word
    for j in range(len(g)):
        if s[j]==g[j]:
            ans+='G'
        else:
            ans+='B'
    print(ans)
    ans=''
    
        # for k in range(0,len(s)):
        #     if s[k]==g[j]:
        #         print("G")
        #     else:
        #         print("B")
    
    