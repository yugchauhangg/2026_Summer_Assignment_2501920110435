#  Q7: Product of digits
n = int(input("Enter number: "))
product = 1
temp = abs(n)
while temp > 0:
    product *= temp % 10
    temp //= 10
print("Product of digits:", product)