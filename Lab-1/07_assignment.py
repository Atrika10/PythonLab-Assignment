#write a program which makes use of function to display all such numbers which are divisible by 7 but are not a multiple of 5 , between 1000 and 2000

def is_divisible_by_7_not_multiple_of_5(n):
    return n % 7 == 0 and n % 5 != 0

for i in range(1000, 2001):
    if is_divisible_by_7_not_multiple_of_5(i):
        print(i, end = " ")
print()






    