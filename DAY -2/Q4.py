# Q8: Check palindrome number
n = int(input("Enter number: "))
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if n == rev:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")