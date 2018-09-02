from sys import exit
print('Celsius(C), Fahrenheit(F), Kelvin(K)')
current_unit = input('Enter the current unit: ')
unit_value = float(input('Enter the number of degrees: '))
desired_conversion = input('Enter the unit you would like to convert to: ')

if current_unit == desired_conversion:
    exit('ERROR: Cannot be converted.')

else:
    if current_unit == 'C' and desired_conversion == 'F':
        degrees = 1.8*unit_value+32
        print(f'The converted value is {degrees}˚{desired_conversion}')
    elif current_unit == 'F' and desired_conversion == 'C':
        degrees = 5/9 * (unit_value - 32)
        print(f'The converted value is {degrees}˚{desired_conversion}')
    elif current_unit == 'K' and desired_conversion == 'C':
        degrees = unit_value - 273.15
        print(f'The converted value is {degrees}˚{desired_conversion}')
    elif current_unit == 'C' and desired_conversion == 'K':
        degrees = unit_value + 273.15
        print(f'The converted value is {degrees}˚{desired_conversion}')
    elif current_unit == 'K' and desired_conversion == 'F':
        degrees = 9/5*(unit_value - 273.15) + 32
        print(f'The converted value is {degrees}˚{desired_conversion}')
    elif current_unit == 'F' and desired_conversion == 'K':
        degrees = 5/9*(unit_value - 32) + 273.15
        print(f'The converted value is {degrees}˚{desired_conversion}')
    