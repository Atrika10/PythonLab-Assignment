# WAP to reverse a given String
str = input("Enter a String : ")
 # logic for reversing a string
rev_str = " "
for i in str:
    rev_str = i + rev_str 
print(f"Reverse of the string is : {rev_str}")
