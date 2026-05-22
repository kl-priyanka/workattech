r, h = map(float, input("Radius, Height? ").split())
pi = 3.14
v = pi * (r**2) * h
price = 40
totalCost = (v * price)/1000
print("{:.2f}".format(totalCost))