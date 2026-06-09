# Q22: Binary to decimal
b = input("Enter binary number: ")
result = 0
for bit in b:
    result = result * 2 + int(bit)
print("Decimal:", result)
