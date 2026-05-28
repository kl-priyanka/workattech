# Write your code here
n = int(input("Enter a number: "))
arr = list(map(int, input("Enter numbers: ").split()))
for a in arr:
	if a%2==0:
		print("EVEN")
	else:
		print("ODD")