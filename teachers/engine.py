import pandas as pd
from persiantools.jdatetime import JalaliDate
import datetime

class Teachers:
    def __init__(self):
        self.teacher_frame = pd.read_csv('datasets/teachers.csv')

    def get_head(self):
        return self.teacher_frame.head()

print(JalaliDate.to_jalali(2013, 9, 16))