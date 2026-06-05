# Q16: Print Armstrong numbers in a range
a = int(input("Enter start: "))
b = int(input("Enter end: "))
for n in range(a, b + 1):
    digits = len(str(n))
    total = sum(int(d) ** digits for d in str(n))
    if total == n:
        print(n, end=" ")