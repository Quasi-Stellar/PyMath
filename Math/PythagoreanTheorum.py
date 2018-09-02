# Required for math functions
import math
# Required for system control
import sys

# Takes user input on sides of triangle
a = float(input('Please choose a length for side A of a right triangle: '))
b = float(input('Please choose a length for side B of a right triangle: '))

# Pythagorean Theorum used to calculate length of hypotenuse c
c = math.sqrt(a**2+b**2)

# Print length c
print("The length of your right triangle's hypotenuse is: ", c)
