from TempDataSet import TempDataSet

docstring = """ TestTempDataSet 
    Submitted by Ye-Hwan Kim
    Submitted: Mar 10, 2021
    This program tests the class TempDataSet.
"""

current_set = TempDataSet()

print("First test of get_num_objects: ", end='')

if TempDataSet.get_num_objects() == 1:
    print("Success")
else:
    print("Fail")

second_set = TempDataSet()

print("Second test of get_num_objects: ", end='')

if TempDataSet.get_num_objects() == 2:
    print("Success")
else:
    print("Fail")

print("Testing get_name and set_name: ")

print("- Default Name:", end='')

if current_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("- Try setting a name too short: ", end='')

try:
    current_set.name = "to"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name too long: ", end='')

try:
    current_set.name = "supercalifragilisticexpialidocious"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name just right (Goldilocks): ", end='')

try:
    current_set.name = "New Name"
    if current_set.name == "New Name":
        print("Success")
    else:
        print("Fail")
except ValueError:
    print("Fail")

print("- Make sure we didn't touch the other object: ", end='')
if second_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("Testing get_avg_temperature_day_time: ", end='')
if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_num_temps: ", end='')
if current_set.get_num_temps(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_loaded_temps: ", end='')
if current_set.get_loaded_temps() is None:
    print("Success")
else:
    print("Fail")

print("Testing get_summary_statistics: ", end='')
if current_set.get_summary_statistics(None) is None:
    print("Success")
else:
    print("Fail")

print("Testing process_file: ", end='')
if current_set.process_file(None) is False:
    print("Success")
else:
    print("Fail")
