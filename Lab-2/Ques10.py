#Write a program in Python to check if a number is Krishnamurthy number.
num = int(input("Enter the number: "))
# checking factorial of each digit
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

# checking if the number is Krishnamurthy number
def is_krishnamurthy(num):
    temp = num
    sum =0
    while temp > 0:
        digit = temp %10
        sum += factorial(digit)
        temp = temp // 10
    if sum == num:
        return True
    else:
        return False

# calling the function & printing the result
if is_krishnamurthy(num):
    print(f"{num} is a Krishnamurthy number")
else:
    print(f"{num} is not a Krishnamurthy number")


        
