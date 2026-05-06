p, r, t = map(float, input("Principal, Rate, Time? ").split())
#p, r, t = map(float, input().split())
interest = (p*r*t)/100
print("{:.6f}".format(interest))