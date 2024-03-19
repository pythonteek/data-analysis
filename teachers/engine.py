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

    def add_jalali_date_to_teacher_frame(self):
        date_create = self.get_date_created()
        print(date_create)

#print(JalaliDate.to_jalali(2013, 9, 16))
T1 = Teachers()
T1.add_jalali_date_to_teacher_frame()