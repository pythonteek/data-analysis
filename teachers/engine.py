import pandas as pd
from persiantools.jdatetime import JalaliDate
from datetime import datetime


class Teachers:
    def __init__(self):
        self.teacher_frame = pd.read_csv('datasets/teachers.csv')

    def get_head(self):
        return self.teacher_frame.head()

    def get_date_created(self):
        return self.teacher_frame['date_created']

    def date_format_convertor(self, date):
        dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        year = dt.year
        month = dt.month
        day = dt.day

        return [year, month, day]
    def add_jalali_date_to_teacher_frame(self):
        date_create = self.get_date_created()
        jalali_date_list = []
        for dc in date_create:
            list_format = self.date_format_convertor(dc)
            curr_jalali_date = JalaliDate.to_jalali(list_format[0], list_format[1], list_format[2])
            jalali_date_list.append(curr_jalali_date)

        self.teacher_frame.insert(2, "jalali_date_created", jalali_date_list, True)

    def number_of_submited_teacher_in_each_month(self):
        self.add_jalali_date_to_teacher_frame()
        df = self.teacher_frame['jalali_date_created']
        for t in df:
            curr_year = t.year
            curr_month = t.month

            y_m = str(curr_year) + "-" + str(curr_month)
            print(y_m)

#print(JalaliDate.to_jalali(2013, 9, 16))
T1 = Teachers()
T1.number_of_submited_teacher_in_each_month()

