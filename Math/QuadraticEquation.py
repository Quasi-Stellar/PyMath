# Required for square root
from math import sqrt

# Takes user input and gets numbers
def qe():
    try: # Tries to convert inputs to floating point numbers
        a = float(input('Please enter a number to represent a: '))
        if a == 0:
            return('ERROR: a cannot be equal to zero.')
        b = float(input('Please enter a number to represent b: '))
        c = float(input('Please enter a number to represent c: '))
    except: # If type conversion failed; such as if an input is a letter
        return('ERROR: Please enter a valid input.')

# Formula to calculate roots
    x1 = (-b + sqrt((b**2) - 4*a*c))/(2*a)
    x2 = (-b - sqrt((b**2) - 4*a*c))/(2*a)

# Prints out values
    print('The Quadratic Roots are: ', x1,  ' and ', x2)
    global kill
    kill = input('To run again, type 1: ')
    if kill != '1':
        kill = False

kill = True
while kill:
    qe()
