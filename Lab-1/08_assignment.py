#write a program to check whether a number is palindrome or not

def is_palindrome(n):
    return str(n) == str(n)[::-1]
    
n = int(input("Enter a number: "))
if is_palindrome(n):
    print("The number is palindrome")
else:
    print("The number is not palindrome")

    