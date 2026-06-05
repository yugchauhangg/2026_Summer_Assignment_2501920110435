# Q14: Nth Fibonacci term
n = int(input("Enter n: "))
a, b = 0, 1
for _ in range(n - 1):
    a, b = b, a + b
print("Nth Fibonacci term:", a)