#  Q9: Check prime number
n = int(input("Enter number: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
print(n, "is prime" if is_prime else "is not prime")