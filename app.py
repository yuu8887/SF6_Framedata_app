import streamlit as st

from SF6_Framedata_ExcelDataManager import ExcelDataManager
from SF6_Framedata_FilterController import FilterController



###################################################
# データ読み込み
###################################################

manager = ExcelDataManager("SF6_FrameData.xlsx")

df = manager.get_dataframe()

controller = FilterController(df)

###################################################
# タイトル
###################################################
st.title("SF6 フレームデータビューワー")

###################################################
# キャラクター選択
###################################################

character = st.selectbox(
    "キャラクター",
    controller.get_character1_list()
)


###################################################
# 検索ボタン
###################################################
if st.button("検索"):
    result = controller.filter_data(
        character1=character
    )
else:

    result = df

###################################################
# 表示
###################################################
st.dataframe(
    result,
    use_container_width=True
)