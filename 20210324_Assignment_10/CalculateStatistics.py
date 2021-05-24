from TempDataSet import TempDataSet

docstring = """ CalculateStatistics
    Submitted by Ye-Hwan Kim
    Submitted: Mar 24, 2021
    This program provides a menu that the user can select from.
    This program creates lists for the sensors and tests changing filters.
    This program reads and stores data from csv files.
    This program displays temperature statistics in different units.
"""

current_unit = 0
UNITS = {0: ("Celsius", "C"), 1: ("Fahrenheit", "F"), 2: ("Kelvin", "K")}


# from assignment 9
def print_filter(sensor_list, active_sensors):
    """ Print the list of sensors and note active ones """
    print("Printing filtered sensor list.")
    for room_number, title, sensor_number in sensor_list:
        print(f"{room_number}: {title}", end="")
        if sensor_number in active_sensors:
            print(" [ACTIVE]")
        else:
            print()


def change_filter(sensor_list, active_sensors):
    """ Edit room filter """
    print("Called change_filter() function.")
    sensors = {}
    for room_number, _, sensor_number in sensor_list:
        sensors[room_number] = sensor_number
    print(f"sensor_dict = {sensors}")
    while True:
        print_filter(sensor_list, active_sensors)
        user_input = input("\nType the sensor number to toggle (e.g.4201) or "
                           "x to end: ")
        if user_input == "x":
            break
        if user_input in sensors:
            input_sensor_number = sensors[user_input]
            print(f"Room {user_input} found {input_sensor_number} in list.")
            if input_sensor_number in active_sensors:
                active_sensors.remove(input_sensor_number)
            else:
                active_sensors.append(input_sensor_number)
        else:
            print(f"Invalid sensor {user_input}. Please try again.")
            continue


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
    file_path = input(
        "Please enter the path and file name of the new dataset: ")
    if dataset.process_file(file_path):
        print(f"Loaded {dataset.get_loaded_temps()} samples.")
        while True:
            name = input("Please enter a 3 to 20 character name for the data: ")
            try:
                dataset.name = name
            except ValueError:
                print("Error: Invalid input.")
            else:
                break
    else:
        print("Error: Unable to load the file.")


def choose_units():
    """ Choose units """
    global current_unit
    print(f"Current units in {UNITS[current_unit][0]}")
    while True:
        print("Choose new units:")
        for key in UNITS:
            print(f"{key} - {UNITS[key][0]}")
        print("Which unit? [Enter 0, 1 or 2]")
        try:
            unit = int(input())
        except ValueError:
            print("Error: Invalid input. Enter a number only.")
        else:
            if unit not in UNITS:
                print("Please choose a unit from the list.")
            else:
                current_unit = unit
                break


def print_summary_statistics(dataset, active_sensors):
    """ Display a summary of the data collected """
    summary = dataset.get_summary_statistics(active_sensors)
    if summary is None:
        print("Please load data file and make sure at least one sensor is "
              "active.")
    else:
        print(f"Summary statistics for {dataset.name}")
        unit = UNITS[current_unit][1]
        print(f"Minimum Temperature: "
              f"{convert_units(summary[0], current_unit):.2f} {unit}")
        print(f"Maximum Temperature: "
              f"{convert_units(summary[1], current_unit):.2f} {unit}")
        print(f"Average Temperature: "
              f"{convert_units(summary[2], current_unit):.2f} {unit}")


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

    sorted_by_room = recursive_sort(the_sensor_list)
    print(f"sensors by room number {sorted_by_room}")
    print(f"active_list is {the_active_sensors}")
    print()

    current_set = TempDataSet()

    print_header()

    while True:
        print()
        print_menu()

        avg_temp = current_set.get_avg_temperature_day_time(the_active_sensors,
                                                            5, 7)
        print(f"The average temperature is {avg_temp}")

        print("Enter [1-7] for the menu option you would like to select:")
        try:
            selection = int(input())
        except ValueError:
            print("Error: Invalid input. Enter a number only.")
        else:
            if selection == 1:
                new_file(current_set)
            elif selection == 2:
                choose_units()
            elif selection == 3:
                change_filter(sorted_by_room, the_active_sensors)
            elif selection == 4:
                print_summary_statistics(current_set, the_active_sensors)
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
