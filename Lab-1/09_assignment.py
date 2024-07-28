#write a program to check whether a number a perfect number and also check wthether the number is armstrong or not

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == n

n = int(input("Enter a number: "))
if is_perfect(n):
    print("The number is perfect")
else:
    print("The number is not perfect")

if is_armstrong(n):
    print("The number is armstrong")
else:
    print("The number is not armstrong")

    