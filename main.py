# %%
import pandas as pd
from datetime import datetime
from collections import defaultdict


class UTAttendance():
    def __init__(self, csv_file_name):
        self.df = pd.read_csv(csv_file_name)

    def calculate_duration(self, date_format='%d/%m/%Y %H:%M:%S'):
        self.df[self.df.columns[-1]] = self.df[self.df.columns[-1]
                                               ].apply(lambda x: datetime.strptime(x, date_format).timestamp())
        self.df[self.df.columns[1]] = self.df[self.df.columns[1]].apply(
            lambda x: datetime.strptime(x, date_format).timestamp())
        self.df.loc[:, 'duration'] = self.df[self.df.columns[-1]] - \
            self.df[self.df.columns[1]]

    def convert_to_hour(self):
        self.df[self.df.columns[-1]] /= 3600

    def sum_durations(self):
        users_durations = defaultdict(lambda: 0)
        for _, item in self.df.iterrows():
            users_durations[int(item[self.df.columns[0]])
                            ] += item[self.df.columns[-1]]
        return pd.DataFrame.from_dict({'user': users_durations.keys(), 'duration': users_durations.values()})

    def save_results(self,filename='results.csv'):
        database.calculate_duration()
        database.convert_to_hour()
        database.sum_durations().to_csv(filename,index=False)


database = UTAttendance('data.csv')
