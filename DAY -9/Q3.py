# Q35: Repeated character pattern
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(chr(64 + i) * i)