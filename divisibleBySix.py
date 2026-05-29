n = int(input("Enter any number: "))
a = list(map(int, input(f"Enter {n} numbers: ").split()))
for i in a:
	if i%6==0:
		print("TRUE")
	else:
		print("FALSE")