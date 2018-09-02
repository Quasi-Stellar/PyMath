# Control over script ending
from sys import exit
# Gets factorial function
from math import factorial

# Gets factorial number
number = int(input("Enter the number you'd like to take the factorial of: "))
if number <= 0:
    exit("Please enter a valid number.")

factorial = factorial(number)
print("The factorial is: ", factorial )
