"""
Author : Dinesh Arockiasamy
Date : 06/14/2020
Project : Traffic violation data analysis

Entry point of the exploratory data analysis of Traffic violation data.
"""

from ViolationInfo import *
from DocWriter import *
import os
import random


def pick_random_states():
    """select three states randomly to search from data set
    This function used containers like list, tuple, set and of course string
    """
    try:
        with open(os.path.join(os.getcwd(), "states.txt"), 'r') as state_file:
            states_str = state_file.read().replace("\n", ",")
    except Exception as error:
        print("State list doesn't exist - {}".format(error))
        return "NJ"
    states_lst = states_str.split(",")
    # list of tuples containing state code and description
    group_code = [tuple(states_lst[i:i + 2]) for i in range(0, len(states_lst), 2)]
    sampling = random.choices(group_code, k=3)
    extract_state_code = [elm[0] for elm in sampling]
    # assigning values to set to remove duplicates
    remove_duplicates = set(extract_state_code)
    return ','.join(remove_duplicates)


def prepare_output_header(datadict):
    """ Writes high level details about the violation data set """
    size = datadict["size"]
    str_content = "Number of rows : " + str(size[0]) + "\n" + \
                  "Number of columns : " + str(size[1]) + "\n" + \
                  "Variables : " + ', '.join(list(datadict['variables']))
    return str_content


def convert_dict_to_string(datadict, hdr):
    """Prepare string content from data dictionary to
    write it to output file"""
    str_content = hdr
    for k, v in datadict.items():
        str_content += k + " : \n" + \
                       '\n'.join(str(item) for item in v.items()) + "\n"
    return str_content


if __name__ == "__main__":
    # Initialize input and output classes
    violation_data = ViolationInfo("Traffic_Violations.csv")
    doc = DocWriter('Output.txt')

    # Unit testing
    test_dict = {"size": (1018634, 35),
                 "variables": ['Date Of Stop', 'Time Of Stop',
                               'Agency', 'SubAgency', 'Description',
                               'Location', 'Latitude', 'Longitude',
                               'Accident', 'Belts', 'Personal Injury',
                               'Property Damage', 'Fatal', 'Commercial License',
                               'HAZMAT', 'Commercial Vehicle', 'Alcohol',
                               'Work Zone', 'State', 'VehicleType',
                               'Year', 'Make', 'Model',
                               'Color', 'Violation Type', 'Charge',
                               'Article', 'Contributed To Accident',
                               'Race', 'Gender',
                               'Driver City', 'Driver State', 'DL State',
                               'Arrest Type', 'Geolocation']}

    test_violation_data = ViolationInfo("No_file.csv")
    test_title = "Traffic Violation Data"
    assert (violation_data == test_violation_data) == False, \
        "Objects are not equal. Result must be False"

    assert violation_data.get_basic_details() == test_dict, \
        "Values must be matching"

    assert str(violation_data) == test_title, "value must be matching"

    # Retrieve basic info of data set
    try:
        data_dict = violation_data.get_basic_details()
        doc.append_content(prepare_output_header(data_dict))
    except Exception as e:
        print("Retrieve header of output failed : {}".format(e))

    # Retrieve accident contributing variables
    header = "\n\nContribute to Accident : \n"
    try:
        data_dict = violation_data.get_accident_stats()
        doc.append_content(convert_dict_to_string(data_dict, header))
    except Exception as e:
        print("Retrieve accident data failed : {}".format(e))

    # Statistics by state
    states = pick_random_states()
    header = "\n\nViolations : \n States : " + states + "\n"
    try:
        data_dict = violation_data.search_violations_by_state(pick_random_states())
        doc.append_content(convert_dict_to_string(data_dict, header))
    except Exception as e:
        print("Retrieve violations by state failed : {}".format(e))

    # Violations by gender
    header = "\n\nViolations : \n Male : \n"
    try:
        data_dict = violation_data.search_violation_by_gender("M")
        doc.append_content(convert_dict_to_string(data_dict, header))
    except Exception as e:
        print("Retrieve violations by gender failed : {}".format(e))
