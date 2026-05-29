t = int(input("Enter the number of test cases: "))
a = list(map(int, input(f"Enter {t} numbers: ").split()))
for i in a:
	if i>7:
		print("UP")
	elif i<7:
		print("DOWN")
	else:
		print("EQUAL")