# Python3 program to find Majority
# element in an array

# Function to find Majority
# element in an array


def findMajority(arr, n):

	maxCount = 0
	index = -1 # sentinels
	for i in range(n):

		count = 1
		# here we compare the element in
		# ith position with i+1th position
		for j in range(i+1, n):

			if(arr[i] == arr[j]):
				count += 1

		# update maxCount if count of
		# current element is greater
		if(count > maxCount):

			maxCount = count
			index = i

	# if maxCount is greater than n/2
	# return the corresponding element
	if (maxCount > n//2):
		print(arr[index])

	else:
		print("No Majority Element")


# Driver code
if __name__ == "__main__":
	arr = [1, 2, 2, 2, 3, 5, 2]
	n = len(arr)

	# Function calling
	findMajority(arr, n)

# This code is contributed
# by ChitraNayal
