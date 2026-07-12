import pandas as pd

class ExcelDataManager:

    def __init__(self, filename):
        self.df = pd.read_excel(filename)

        self.df = self.df.fillna("")
        self.df = self.df.astype(str)

    def get_dataframe(self):
        return self.df