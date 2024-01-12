# cook your dish here
t=int(input())
for _ in range(t):
    x=input()
    a="Sad"
    for i in range(len(x)):
        if x[i] in {'a','e','i','o','u'}:
            if x[i+1] in {'a','e','i','o','u'}:
               if x[i+2] in {'a','e','i','o','u'}:
                   a="Happy"
                   break
    print(a) 