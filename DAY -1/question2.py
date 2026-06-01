# Write a program to Print multiplication table of a given number.
num = int(input("Enter a number: ")) # take the input from the user


for i in range(1, 11): # loop from 1 to 10
    print(f"{num} x {i} = {num * i}") # print the table for the given number
    
