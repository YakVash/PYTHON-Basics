# Program to calculate the sum of integers from 1 to n
n = int(input("Enter a positive integer n: "))

if n <= 0:

	print("Please enter a positive value")

else:

	sum = 0

for i in range(1, n + 1):

    		sum += i

print("The sum of integers from 1 to", n, "is : ", sum)