import pandas as pd

class ExcelDataManager:

    def __init__(self, filename):
        self.df = pd.read_excel(filename)

    def get_dataframe(self):
        return self.df