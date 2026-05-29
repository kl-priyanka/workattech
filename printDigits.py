n = int(input("Enter a number: "))
a = list(map(int, input(f"Enter the {n} numbers: ").split()))
for i in a:
	result = " ".join(map(str, str(i)))
	print(result)