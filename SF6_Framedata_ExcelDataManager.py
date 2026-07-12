import pandas as pd

def __init__(self, filename):

        # Excelを読み込む
        self.df = pd.read_excel(
            filename,
            dtype=object
        )

        # 空欄を空文字にする
        self.df = self.df.fillna("")

        # 全列をPython標準の文字列(str)へ変換
        for col in self.df.columns:

            self.df[col] = (
                self.df[col]
                .apply(str)
                .str.replace(".0", "", regex=False)
            )

        # 列名も念のためstrへ変換
        self.df.columns = [
            str(col)
            for col in self.df.columns
        ]


def get_dataframe(self):

        return self.df.copy()