#write a program to display reverse of a number

num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10
print(f"The reverse of the number is: {rev}")
