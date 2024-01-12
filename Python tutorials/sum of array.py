arr=[1,3,4,5,7]
sum=6
for i in range(len(arr)):
    for j in range(len(arr)):
        z=arr[i]+arr[j]
        if z==sum:
            print(f'({arr[i]},{arr[j]})',end='')