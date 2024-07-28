#Write a program to find area and perimeter of a rectangle.
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)

print(f"The area of the rectangle is {area} and the perimeter of the rectangle is {perimeter}")