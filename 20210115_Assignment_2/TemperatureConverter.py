docstring = """ Temperature Converter
    Submitted by Ye-Hwan Kim
    Submitted: Jan 15, 2021
    This program prompts the user for a temperature in Celsius and converts the
    temperature to a specified temperature unit.
"""


def print_header():
    print("Temperature Project")
    print("Ye-Hwan Kim")


def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value
    elif units == 1:
        fahrenheit_value = celsius_value * 9 / 5 + 32
        return fahrenheit_value
    elif units == 2:
        kelvin_value = celsius_value + 273.15
        return kelvin_value


if __name__ == '__main__':
    print_header()
    print("Please enter a temperature in degrees Celsius:")
    celsius = float(input())
    fahrenheit = convert_units(celsius, 1)
    print(f"That's {fahrenheit} degrees Fahrenheit and")
    kelvin = convert_units(celsius, 2)
    print(f"{kelvin} Kelvin")
