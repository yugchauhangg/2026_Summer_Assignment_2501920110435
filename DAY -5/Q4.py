# Q20: Find largest prime factor
n = int(input("Enter number: "))
largest = -1
d = 2
temp = n
while d * d <= temp:
    while temp % d == 0:
        largest = d
        temp //= d
    d += 1
if temp > 1:
    largest = temp
print("Largest prime factor:", largest)