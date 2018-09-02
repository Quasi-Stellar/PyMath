# Controll over exiting
import sys

# Get math function
print("Available Processes: Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), Exponent(**)")
option = input("Please enter the symbol of a process above: ")

if (option == "+"):
    a = float(input("First number to add: "))
    b = float(input("Second number to add: "))
    sum = a + b
    print("The sum is: ", sum)

elif (option == "-"):
    a = float(input("First number to subtract: "))
    b = float(input("Second number to subtract: "))
    difference = a - b
    print("The difference is: ", difference)

elif (option == "*"):
    a = float(input("First number to multiply: "))
    b = float(input("Second number to add: "))
    product = a*b
    print("The product is: ", product)

elif (option == "/"):
    a = float(input("First number to divide: "))
    b = float(input("Second number to divide: "))
    quotient = a/b
    print("The quotient is: ", quotient)

elif (option == "%"):
    a = int(input("First number to divide: "))
    b = int(input("Second number to divide: "))
    quotient = int(a/b)
    mod = a%b
    print("The remainder is: ", quotient, "R", mod)

elif (option == "**"):
    a = float(input("Number to multiply by itself: "))
    b = float(input("Raised to the power of: "))
    simplified_version = a**b
    print("The simplified version is: ", simplified_version)

else:
    sys.exit("ERROR: Not an available option.")