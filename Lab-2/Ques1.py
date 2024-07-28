# To find the square root of any three numbers
# function to find the square root of a number
def sqrt(num):
    return num**0.5

# take input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# calculate the square root of the numbers
sum = sqrt(num1) + sqrt(num2) + sqrt(num3)
print("The sum of the square root of the three numbers is: ", sum)