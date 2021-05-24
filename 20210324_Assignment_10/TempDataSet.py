import math

docstring = """ TempDataSet 
    Submitted by Ye-Hwan Kim
    Submitted: Mar 24, 2021
    This class manages temperature data.
"""


# from assignment 9
class TempDataSet:
    num_dataset_objects = 0

    def __init__(self):
        self._data_set = None
        self._name = "Unnamed"
        TempDataSet.num_dataset_objects += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        length = len(new_name)
        if length < 3 or length > 20:
            raise ValueError
        self._name = new_name

    def process_file(self, filename):
        """ Process a new data file """
        try:
            file = open(filename)
        except FileNotFoundError:
            return False
        else:
            self._data_set = []
            for line in file:
                my_tuple = tuple(line.split(","))
                if my_tuple[3] == "TEMP":
                    day = int(my_tuple[0])
                    time = math.floor(float(my_tuple[1]) * 24)
                    sensor = int(my_tuple[2])
                    temp = float(my_tuple[4])
                    self._data_set.append((day, time, sensor, temp))
            file.close()
            return True

    def get_summary_statistics(self, active_sensors):
        """ Get the minimum, maximum, and average temperatures """
        if (self._data_set is None) or (active_sensors is None) or (len(
                active_sensors) == 0):
            return None
        else:
            match = [line for line in self._data_set if line[2] in
                     active_sensors]
            temp_min = 100
            temp_max = -100
            temp_sum = 0
            for line in match:
                temp = line[3]
                if temp < temp_min:
                    temp_min = temp
                if temp > temp_max:
                    temp_max = temp
                temp_sum += temp
            return temp_min, temp_max, temp_sum / len(match)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """ Get the average of temperatures on a specific day and time """
        if (self._data_set is None) or (active_sensors is None) or (len(
                active_sensors) == 0):
            return None
        else:
            match = [line for line in self._data_set if line[0] == day and
                     line[1] == time and line[2] in active_sensors]
            temp_sum = 0
            for line in match:
                temp_sum += line[3]
            return temp_sum / len(match)

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        """ (Unimplemented method) """
        if self._data_set is None:
            return None
        else:
            return 0

    def get_num_objects(self):
        """ (Unimplemented method) """
        if self._data_set is None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        """ Return the number of samples created """
        if self._data_set is None:
            return None
        else:
            return len(self._data_set)

    @classmethod
    def get_num_objects(cls):
        """ Return the number of objects created """
        return TempDataSet.num_dataset_objects
