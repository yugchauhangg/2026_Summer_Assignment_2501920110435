# Q24: Find x^n without pow()
x = int(input("Enter base x: "))
n = int(input("Enter exponent n: "))
result = 1
for _ in range(n):
    result *= x
print(f"{x}^{n} =", result)