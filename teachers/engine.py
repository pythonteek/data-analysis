import pandas as pd
from persiantools.jdatetime import JalaliDate
import datetime

class Teachers:
    def __init__(self):
        self.teacher_frame = pd.read_csv('datasets/teachers.csv')

    def get_head(self):
        return self.teacher_frame.head()

    def get_date_created(self):
        return self.teacher_frame['date_created']

#print(JalaliDate.to_jalali(2013, 9, 16))
T1 = Teachers()
print(T1.get_date_created())