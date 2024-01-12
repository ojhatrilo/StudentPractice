import random
start=int(input("enter the upper limit:"))
end=int(input("enter the upper limit:"))
ran=random.randint(start,end)
limit=5
for i in range(5):
    number=int(input("enter your guess:"))
    if ran==number:
        print("you won")
        break
    else:
        print("your gusse is wrong")
   
print(f'the correct number is {ran}')

