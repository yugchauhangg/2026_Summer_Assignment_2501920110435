#  Sum of digits of a number
n = int(input("Enter number: "))
s = 0
temp = abs(n)
while temp > 0:
    s += temp % 10
    temp //= 10
print("Sum of digits:", s)