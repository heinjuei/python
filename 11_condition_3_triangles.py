# Triangle repeat commands
# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides the same length.
# Equilateral triangle: All sides are equal.

a = int(input("The length of side a = "))

while a < 0:
    print(int("Please insert a positive number:"))
    
b = int(input("The length of side b = "))

while b < 0:
    print(int("Please insert a positive number:"))

c = int(input("The length of side c = "))
while c < 0:
    print(int("Please insert a positive number:"))

    
if a != b and b != c and a != c:
 print("This a scalene triangle.")
elif a == b and b == c:
 print("This is an equilateral triangle.")
else:
 print("This is an isosceles triangle.")

