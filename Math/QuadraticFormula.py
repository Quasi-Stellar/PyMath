# Required for math.sqrt
from math import sqrt
# Required to end program if error occurs
import sys

# Takes user input and gets numbers
a = float(input('Please enter a number to represent a: '))
if a == 0:
    sys.exit('ERROR: a cannot be equal to zero.')
b = float(input('Please enter a number to represent b: '))
c = float(input('Please enter a number to represent c: '))

# Formula to calculate roots
x1 = (-b + sqrt((b**2) - 4*a*c))/(2*a)
x2 = (-b - sqrt((b**2) - 4*a*c))/(2*a)

# Prints out values
print('The Quadratic Roots are: ', x1,  ' and ', x2)
