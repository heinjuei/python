# Functions (sphere)
"""Returns the volume of a sphere with radiu r."""
#import math
#dir(math)
#math.pi
#def volume(r):
#	v = (4.0/3.0) * math.pi * r**3
#	return v
#volume(2)


""" Return the area of a triangle with base b and height h."""
#def triangle_area(b, h):
#	0.5 * b * h
#triangle_area(3,6)

# Keyword arguments
""" Converts a length from feet and inches to centimeters."""
#def cm(feet = 0, inches = 0):
#inches_to_cm = inches * 2.54
#feet_to_cm = feet * 12 * 2.54
#return inches_to_cm + feet_to_cm

#cm(feet = 5)
#cm(inches = 70)

# Required arguments

def g(y, x = 0):
    return x + y
g(5)
g(7, x = 3)
