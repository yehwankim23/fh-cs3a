docstring = """ TempDataSet 
    Submitted by Ye-Hwan Kim
    Submitted: Mar 10, 2021
    This class manages temperature data.
"""


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
        """ (Unimplemented method) """
        return False

    def get_summary_statistics(self, active_sensors):
        """ (Unimplemented method) """
        if self._data_set is None:
            return None
        else:
            return 0, 0, 0

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """ (Unimplemented method) """
        if self._data_set is None:
            return None
        else:
            return 0

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
        """ (Unimplemented method) """
        if self._data_set is None:
            return None
        else:
            return 0

    @classmethod
    def get_num_objects(cls):
        """ Return the number of objects created """
        return TempDataSet.num_dataset_objects
