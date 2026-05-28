weights = list(map(float, input("Enter the weights: ").split()))
avg_weight = sum(weights) / len(weights)
print(f"The average weight is: {avg_weight:.6f}")