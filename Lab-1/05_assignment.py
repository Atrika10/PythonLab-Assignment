#write a program to find factorial of a number

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(f"The factorial of {num} is: {fact}")
