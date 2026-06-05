# Q18: Check strong number
n = int(input("Enter number: "))
total = 0
temp = n
while temp > 0:
    d = temp % 10
    fact = 1
    for i in range(1, d + 1):
        fact *= i
    total += fact
    temp //= 10
print(n, "is strong" if total == n else "is not strong")
