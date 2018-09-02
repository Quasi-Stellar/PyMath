# Asks for all the primes under this number.
max = int(input("Enter a number to find primes up to: "))

# Tests all numbers to be primes
for x in range(2, max + 1):
    isPrime = True
    for y in range(2, x):
        if x % y == 0:
            isPrime = False
    # Prints primes
    if isPrime:
        print(x)