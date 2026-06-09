# Q21: Decimal to binary
n = int(input("Enter decimal number: "))
result = ""
temp = n
while temp > 0:
    result = str(temp % 2) + result
    temp //= 2
print("Binary:", result if result else "0")