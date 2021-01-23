docstring = """ Dashboard
    Submitted by Ye-Hwan Kim
    Submitted: Jan 21, 2021
    This program prompts the user for a menu selection, validates the input, 
    and calls appropriate stub functions.
"""


def print_header():
    """ Print program and author's name """
    print("Temperature Project")
    print("Ye-Hwan Kim")


# from assignment 2
def convert_units(celsius_value, units):
    """ Convert given temperature to the specified unit """
    if units == 0:
        return celsius_value
    elif units == 1:
        fahrenheit_value = celsius_value * 9 / 5 + 32
        return fahrenheit_value
    elif units == 2:
        kelvin_value = celsius_value + 273.15
        return kelvin_value


def print_menu():
    """ Print menu to console """
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


def new_file(dataset):
    """ Process a new data file """
    print("Called new_file() function.")


def choose_units():
    """ Choose units """
    print("Called choose_units() function.")


def change_filter(sensor_list, active_sensors):
    """ Edit room filter """
    print("Called change_filter() function.")


def print_summary_statistics(dataset, active_sensors):
    """ Show summary statistics """
    print("Called print_summary_statistics() function.")


def print_temp_by_day_time(dataset, active_sensors):
    """ Show temperature by date and time """
    print("Called print_temp_by_day_time() function.")


def print_histogram(dataset, active_sensors):
    """ Show histogram of temperatures """
    print("Called print_histogram() function.")


def main():
    print_header()
    print_menu()
    while True:
        print("Enter [1-7] for the menu option you would like to select:")
        try:
            selection = int(input())
        except ValueError:
            print("Error: Invalid input. Enter a number only.")
        else:
            if selection == 1:
                new_file(None)
            elif selection == 2:
                choose_units()
            elif selection == 3:
                change_filter(None, None)
            elif selection == 4:
                print_summary_statistics(None, None)
            elif selection == 5:
                print_temp_by_day_time(None, None)
            elif selection == 6:
                print_histogram(None, None)
            elif selection == 7:
                print("Thank you for using the Temperature Project")
                break
            else:
                print("Invalid selection.")


if __name__ == '__main__':
    main()
