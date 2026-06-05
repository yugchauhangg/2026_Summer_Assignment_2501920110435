# Q15: Check Armstrong number
n = int(input("Enter number: "))
digits = len(str(n))
total = sum(int(d) ** digits for d in str(n))
print(n, "is Armstrong" if total == n else "is not Armstrong")