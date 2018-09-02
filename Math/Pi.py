# Control code execution
import sys

pi = 3.14159265359

# Gets the radius of a circle
r = float(input("Enter the radius of a circle: "))

# Makes sure the user is not entering a number that does not have a positive value
if r <= 0:
    sys.exit("ERROR: Radius is an invalid value")

# Calculate values
area = pi*r**2
circumference = pi*r*2
diameter = r*2

# Print values
print("The area is: ", area)
print("The circumference is: ", circumference)
print("The diameter is: ", diameter)