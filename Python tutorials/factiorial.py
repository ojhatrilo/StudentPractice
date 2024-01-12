# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()

def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return num * factorial(num-1)

print(factorial(3))