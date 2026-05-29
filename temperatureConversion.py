n = int(input("Enter any number: "))
a = list(map(float, input(f"Enter {n} values (in celsius): ").split()))
for i in a:
	fah = ((9*i)/5)+32
	print(f"{fah:.2f}")