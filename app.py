import streamlit as st

from SF6_Framedata_ExcelDataManager import ExcelDataManager

st.title("SF6 フレームデータ検索")

excel = ExcelDataManager("SF6_FrameData.xlsx")

df = excel.get_dataframe()

st.dataframe(df)