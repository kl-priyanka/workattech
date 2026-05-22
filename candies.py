candies, cousins = map(int, input("Candies, cousins? ").split())
if cousins == 0:
    print("NO")
else:
    if candies%cousins==0:
        print("YES")
    else:
        print("NO")