# Q23: Count set bits (1s) in a number
n = int(input("Enter number: "))
count = 0
temp = n
while temp > 0:
    count += temp & 1
    temp >>= 1
print("Set bits:", count)
