#write a program to convert temparature from celsius to farenheit
#f = c*1.8 + 32

def c_to_f(c):
    f = c*1.8 + 32
    return f

c= float(input("Enter the temparature in celsius: "))
f = c_to_f(c)
print(f"The temparature in farenheit is: {round(f,2)}")