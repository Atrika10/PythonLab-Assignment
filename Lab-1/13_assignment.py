# Write a program to change temperature from Fahrenheit to Celsius.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0/9.0
print(f"The temperature in Celsius is {round(celsius,2)}")