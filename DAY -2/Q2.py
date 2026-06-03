# Q6: Reverse a number
n = int(input("Enter number: "))
rev = 0
temp = abs(n)
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed number:", rev)