#write a program to generate prime number series upto n

n = int(input("Enter the value of n: "))
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
print()
