"""
########
Class containing attributes and methods to retrieve data and stats from
Traffic violation csv file.
########
"""

import os
import numpy as np
import pandas as pd


class ViolationInfo:
    """Class containing attributes and methods to retrieve
    traffic violation data"""
    title = "Traffic Violation Data"

    def __init__(self, filename):
        self.__file_name = filename
        self.headers = {}
        try:
            self.data_set = pd.read_csv(os.path.join(os.getcwd(),
                                                     self.__file_name))
        except Exception as e:
            self.data_set = None
            print("Error while loading input file : {}".format(e))

    def get_basic_details(self):
        """Retrieve basic information about data set"""
        if self.data_set is not None:
            self.headers = {"size": self.data_set.shape,
                            "variables": list(self.data_set.columns)}
            return self.headers
        else:
            return {"size": "0", "variables": ["No column to display"]}

    def get_accident_stats(self):
        """Retrieve statistics of variables which leads to accident"""
        if self.data_set is not None:
            sub_df = pd.DataFrame(
                zip(self.data_set['Contributed To Accident'],
                    self.data_set['Alcohol'],
                    self.data_set['Belts'],
                    self.data_set['Fatal']),
                columns=['Contributed To Accident',
                         'alcohol',
                         'belts',
                         'fatal'])
            sub_df['alcohol'] = sub_df.alcohol.eq('Yes').mul(1)
            sub_df['belts'] = sub_df.belts.eq('Yes').mul(1)
            sub_df['fatal'] = sub_df.fatal.eq('Yes').mul(1)
            table = pd.pivot_table(sub_df,
                                   values=['alcohol', 'belts', 'fatal'],
                                   columns='Contributed To Accident',
                                   aggfunc=np.mean).to_dict()
            return table

    def search_violation_by_gender(self, gender):
        """Retrieve statistics of variables which leads to violation ticket"""
        if self.data_set is not None:
            filter_condition = self.data_set.Gender == gender
            filtered_df = self.data_set[filter_condition]
            sub_df1 = pd.DataFrame(zip(filtered_df['Violation Type'],
                                       filtered_df['Alcohol'],
                                       filtered_df['Belts'],
                                       filtered_df['Fatal']),
                                   columns=['Violation Type',
                                            'alcohol',
                                            'belts',
                                            'fatal'])
            sub_df1['alcohol'] = sub_df1.alcohol.eq('Yes').mul(1)
            sub_df1['belts'] = sub_df1.belts.eq('Yes').mul(1)
            sub_df1['fatal'] = sub_df1.fatal.eq('Yes').mul(1)
            table = pd.pivot_table(sub_df1,
                                   values=['alcohol', 'belts', 'fatal'],
                                   columns='Violation Type',
                                   aggfunc=np.mean).to_dict()
            return table

    def search_violations_by_state(self, state):
        """Search csv file for a particular state and a parameter"""
        state_lst = str(state).split(',')
        if self.data_set is not None:
            filter_condition = self.data_set.State.isin(state_lst)
            filtered_df = self.data_set[filter_condition]
            sub_df1 = pd.DataFrame(zip(filtered_df['Violation Type'],
                                       filtered_df['Alcohol'],
                                       filtered_df['Belts'],
                                       filtered_df['Fatal']),
                                   columns=['Violation Type',
                                            'alcohol',
                                            'belts',
                                            'fatal'])
            sub_df1['alcohol'] = sub_df1.alcohol.eq('Yes').mul(1)
            sub_df1['belts'] = sub_df1.belts.eq('Yes').mul(1)
            sub_df1['fatal'] = sub_df1.fatal.eq('Yes').mul(1)
            table = pd.pivot_table(sub_df1,
                                   values=['alcohol', 'belts', 'fatal'],
                                   columns='Violation Type',
                                   aggfunc=np.mean).to_dict()
            return table

    def __str__(self):
        return ViolationInfo.title

    def __eq__(self, other):
        if self.data_set is not None and other.data_set is not None:
            return self.data_set == other.data_set
        else:
            return False
