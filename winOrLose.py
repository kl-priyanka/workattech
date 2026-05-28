n = int(input("Enter a number: "))
arr = list(map(int, input("Enter the array elements: ").split()))
arr.sort()
if arr[-1]%2 == 0:
    print("Win")
else:
    print("Lose")