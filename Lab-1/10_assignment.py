#write a program to generate fibonacci series upto n 

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b
    print()

n = int(input("Enter a number: "))
fibonacci(n)
