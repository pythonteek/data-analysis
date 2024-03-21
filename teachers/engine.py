import pandas as pd
from persiantools.jdatetime import JalaliDate
from datetime import datetime
from itertools import groupby



class Teachers:
    def __init__(self):
        print("Teachers constructor is called!")
        self.teacher_frame = pd.read_csv('datasets/teachers.csv')

    # Get head of dataset
    def get_head(self):
        return self.teacher_frame.head()

    # Return DATE_CREATED clolumn
    def get_date_created(self):
        return self.teacher_frame['date_created']

    # Return %Y-%m-%d %H:%M:%S to array as [year, month, day]
    # JalaliDate.to_jalali(2023, 03, 21) -> [1403, 01, 02]
    def date_format_convertor(self, date):
        dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        year = dt.year
        month = dt.month
        day = dt.day

        return [year, month, day]

    # Get data from date_format_convertor and convert it to jalali date
    # This function add new column to dataset
    def add_jalali_date_to_teacher_frame(self):
        date_create = self.get_date_created()
        jalali_date_list = []
        for dc in date_create:
            list_format = self.date_format_convertor(dc)
            curr_jalali_date = JalaliDate.to_jalali(list_format[0], list_format[1], list_format[2])
            jalali_date_list.append(curr_jalali_date)

        self.teacher_frame.insert(2, "jalali_date_created", jalali_date_list, True)

    # How many teachers are submited in each month?
    def number_of_submited_teacher_in_each_month(self):
        self.add_jalali_date_to_teacher_frame()# Add new column to dataset
        df = self.teacher_frame['jalali_date_created']
        y_m_list = []
        for t in df:
            curr_year = t.year
            curr_month = t.month

            y_m = str(curr_year) + "-" + str(curr_month)
            y_m_list.append(y_m)

        print(y_m_list)
        res = [list(val) for key, val in groupby(sorted(y_m_list))]# Make group
        resault = []
        for curr_res in res:
            r = [curr_res[0], len(curr_res)]# Number of elements in each group
            resault.append(r)

        return resault

    # Number of teachers with same degree
    def teachers_degree_clasification(self):
        df = self.teacher_frame['educational degree']
        resault = []
        res = [list(val) for key, val in groupby(sorted(df))]#make group
        for curr_res in res:
            r = [curr_res[0], len(curr_res)]
            resault.append(r)

        return resault

    # Number of teachers with same major
    def teachers_major_clasification(self):
        df = self.teacher_frame['major']
        resault = []
        res = [list(val) for key, val in groupby(sorted(df))]#make group
        for curr_res in res:
            r = [curr_res[0], len(curr_res)]
            resault.append(r)

        return resault
