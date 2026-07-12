import pandas as pd

class ExcelDataManager:
    def __init__(self, filename):

        # Excelを読み込む
        self.df = pd.read_excel(
            filename,
            dtype=object
        )

        # 空欄を空文字にする
        self.df = self.df.fillna("")

        # 全セルを文字列へ変換
        for col in self.df.columns:

            self.df[col] = self.df[col].apply(self.convert_value)

        # 列名も文字列へ
        self.df.columns = [
            str(col)
            for col in self.df.columns
        ]

    def convert_value(self, value):

        if pd.isna(value):
            return ""

        if isinstance(value, float):

            if value.is_integer():
                return str(int(value))

        return str(value)


    def get_dataframe(self):

        return self.df.copy()