from math import sqrt
 
def quadratic():
    try: # Tries to convert inputs to floating point numbers
        a = float(input('Please enter a number to represent a: '))
        if a == 0:
            print('Undefined')
            return
        b = float(input('Please enter a number to represent b: '))
        c = float(input('Please enter a number to represent c: '))
    except: # If type conversion failed; such as if an input is a letter
        print('ERROR: Please enter a valid input.')
        return
 
# Formula to calculate roots
    x1 = (-b + sqrt((b**2) - 4*a*c))/(2*a)
    x2 = (-b - sqrt((b**2) - 4*a*c))/(2*a)
 
# Prints out values
    print(f'The Quadratic Roots are: {x1} and {x2}')
    global kill
    kill = input('To exit this program type any key other than 1. To run again, type 1: ')
    if kill != '1':
        kill = True
 
kill = False
while not kill:
    quadratic()
