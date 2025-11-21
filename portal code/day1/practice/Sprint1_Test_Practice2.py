prodA = list(map(int, input("Enter counts for Product A: ").split(",")))
prodB = list(map(int, input("Enter counts for Product B: ").split(",")))
prodC = list(map(int, input("Enter counts for Product C: ").split(",")))
prodD = list(map(int, input("Enter counts for Product D: ").split(",")))

A_total = sum(prodA)
B_total = sum(prodB)
C_total = sum(prodC)
D_total = sum(prodD)

total = A_total + B_total + C_total + D_total

p_25_A = prodA[0] / total
p_25_A = round(p_25_A, 4)
print()
print("Probability of Product A by someone aged < 25:", p_25_A)
p_C_25_40 = prodC[1] / C_total
p_C_25_40 = round(p_C_25_40, 4)
print("Probability of age 25-40 given Product C purchase:", p_C_25_40)
p_41_60 = (prodA[2] + prodB[2] + prodC[2] + prodD[2]) / total
p_41_60 = round(p_41_60, 4)
print("Overall probability of buyer from 41-60 age group:", p_41_60)

p_B_60 = prodB[3] / total
p_B_60 = round(p_B_60, 4)
print("\nP(Product B and Age 60+):", p_B_60)
p_B = B_total / total
print(f"    P(Product B): {p_B:.4f}")
p_60 = (prodA[3] + prodB[3] + prodC[3] + prodD[3]) / total
print(f"    P(Age 60+): {p_60:.4f}")
p_B_60 = p_B * p_60
print(f"    P(Product B) * P(Age 60+): {p_B_60:.4f}")

print("Conclusion: Product B purchases and Age 60+ are DEPENDENT.")
