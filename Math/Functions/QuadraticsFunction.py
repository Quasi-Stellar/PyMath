# Controlls end of program
from sys import exit

# Used for square root function
from math import sqrt

# Quadratic Function
def quadratic(a,b,c):
    '''
    Quadratic Equation Solver Function
    '''

    x1 = (-b + sqrt((b**2) - 4*a*c))/(2*a)
    x2 = (-b - sqrt((b**2) - 4*a*c))/(2*a)
    return(f'The roots are {x1} and {x2}')

    # Gets values for a,b,c
    a = float(input('Enter the value of a: '))
    if a == 0:
        exit('Undefined.')
    b = float(input('Enter the value of b: '))
    c = float(input('Enter the value of c: '))

    # Calls function
    root = quadratic(a,b,c)
    if b**2 - 4ac >= 0:
        print(root)
    else:
        print('Invalid values')
