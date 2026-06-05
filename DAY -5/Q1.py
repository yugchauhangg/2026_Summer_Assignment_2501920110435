# Q17: Check perfect number
n = int(input("Enter number: "))
total = sum(i for i in range(1, n) if n % i == 0)
print(n, "is perfect" if total == n else "is not perfect")