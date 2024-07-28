# Write a function to calculate the power of a number using recursion
num = int(input("Enter the number: "))
power = int(input("Enter the power: "))
def power_of_num(num, power):
    if power == 0:
        return 1
    else:
        return num * power_of_num(num, power-1)
print(f"The power of {num} raised to {power} is {power_of_num(num, power)}")