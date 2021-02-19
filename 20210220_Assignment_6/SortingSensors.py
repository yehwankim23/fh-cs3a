docstring = """ SortingSensors
    Submitted by Ye-Hwan Kim
    Submitted: Feb 20, 2021
    This program provides a menu that the user can select from.
    This program creates lists for the sensors and tests bubble sort.
"""


def recursive_sort(list_to_sort, key=0):
    """ Bubble sort list recursively """
    length = len(list_to_sort)
    return_value = list_to_sort[0:length]
    changed = False
    for i in range(length - 1):
        if return_value[i][key] > return_value[i + 1][key]:
            (return_value[i + 1], return_value[i]) = (
                return_value[i], return_value[i + 1])
            changed = True
    if changed:
        return_value = recursive_sort(return_value[:length - 1],
                                      key) + return_value[length - 1:length]
    return return_value


# from assignment 4
def print_header():
    """ Print program and author's names """
    print("Temperature Project")
    print("Ye-Hwan Kim")


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


def main():
    the_sensor_list = [("4213", "STEM Center", 0),
                       ("4201", "Foundations Lab", 1),
                       ("4204", "CS Lab", 2),
                       ("4218", "Workshop Room", 3),
                       ("4205", "Tiled Room", 4),
                       ("Out", "Outside", 10)]
    the_active_sensors = [the_sensor_list[item][2] for item in
                          range(len(the_sensor_list))]

    print(f"sensor_list is {the_sensor_list}")
    print(f"active_list is {the_active_sensors}")

    sorted_by_room = recursive_sort(the_sensor_list)
    print(f"sorted list by room number {sorted_by_room}")
    sorted_by_name = recursive_sort(the_sensor_list, 1)
    print(f"sorted list by room name {sorted_by_name}")

    print(f"sensor_list is {the_sensor_list}")
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


if __name__ == "__main__":
    main()
