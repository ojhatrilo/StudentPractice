n=int(input("enetr the numbe"))

for row in range(0, n):
	for col in range(0, n):			
		if (row == col):
			print(n, end=" ")
		else:
			print("*", end=" ")
	print()

	


