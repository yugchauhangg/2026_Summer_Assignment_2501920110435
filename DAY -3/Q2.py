#  Q10: Print prime numbers in a range
a = int(input("Enter start: "))
b = int(input("Enter end: "))
for n in range(a, b + 1):
    if n < 2:
        continue
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")