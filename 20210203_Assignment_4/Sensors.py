docstring = """ Sensors
    Submitted by Ye-Hwan Kim
    Submitted: Jan 28, 2021
    This program prompts the user for a menu selection, validates the input, 
    and calls appropriate stub functions.
    This program creates lists for the sensors and tests their correctness.
"""


def test_sensor_setup(sensor_list, active_sensors):
    """ Determine if the container objects are set up correctly """
    print(f"sensor_list is {sensor_list}")
    print(f"active_list is {active_sensors}")

    print("\nTesting sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list content:")
    rooms_list = [i[0] for i in sensor_list]
    descriptions_list = [i[1] for i in sensor_list]
    if "4213" not in rooms_list or "Out" not in rooms_list:
        print("Fail - something is wrong with the room numbers")
    elif "Foundations Lab" not in descriptions_list:
        print("Fail - something is wrong with room descriptions")
    else:
        print("Pass")

    print("Testing active_sensors length:")
    if len(active_sensors) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing active_sensors content:")
    if sum(active_sensors) == 20:
        print("Pass")
    else:
        print("Fail")


# from assignment 3
def print_header():
    """ Print program and author's name """
    print("Temperature Project")
    print("Ye-Hwan Kim")


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
    sensor_list = [("4213", "STEM Center", 0),
                   ("4201", "Foundations Lab", 1),
                   ("4204", "CS Lab", 2),
                   ("4218", "Workshop Room", 3),
                   ("4205", "Tiled Room", 4),
                   ("Out", "Outside", 10)]
    active_sensors = [sensor_list[item][2] for item in range(len(sensor_list))]
    test_sensor_setup(sensor_list, active_sensors)
    print()

    print_header()
    print()

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
