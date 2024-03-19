import pandas as pd

class Teachers:
    def __init__(self):
        self.teacher_frame = pd.read_csv('datasets/teachers.csv')

    def get_head(self):
        return self.teacher_frame.head()

T1 = Teachers()
print(T1.get_head())