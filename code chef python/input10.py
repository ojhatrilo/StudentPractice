l=['a','e','i','o','u','A','E','I','O','U']
s=input()
s+=" "
s1=""
if len(s)==0:
    print("")
elif len(s)==1:
    if s[0] not in l:
        print(s)
else:
    if s[0] in l and s[1] in l:
        s1+=s[0]
    elif s[0] not in l :
        s1+=s[0]
 
    for i in range(1,len(s)-1):
        if s[i-1] not in l and s[i] in l and s[i+1] not in l:
            continue
        s1+=s[i]
 
    print(s1)