# Q19: Print factors of a number
n = int(input("Enter number: "))
print("Factors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")