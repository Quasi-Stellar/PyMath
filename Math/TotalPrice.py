# Gets Numbers
cost = float(input("Please enter the cost of your item: "))
tax = float(input("Please enter the tax rate: "))

# Calculates total
total = round(cost + (tax*cost), 2)

print(f"The total price is: ${total}")