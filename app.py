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

character2 = st.selectbox(
    "キャラクター(比較用)",
    controller.get_character2_list()
)

operation = st.selectbox(
    "操作タイプ",
    controller.get_operation_type_list()
)

movetype = st.selectbox(
    "技タイプ",
    controller.get_movetype_type_list()
)

command = st.selectbox(
    "コマンド",
    controller.get_command_list()
)

cancel = st.selectbox(
    "キャンセル",
    controller.get_cancel_list()
)

zokusei = st.selectbox(
    "属性",
    controller.get_zokusei_list()
)


startup = st.text_input(
    "発生(数値入力)",
    value=""
)

startup = startup.strip()
if startup == "":
    startup = None

hitF = st.text_input(
    "ヒット時硬直差(数値入力)",
    value=""
)

hitF = hitF.strip()
if hitF == "":
    hitF = None

guardF = st.text_input(
    "ガード時硬直差(数値入力)",
    value=""
)

guardF = guardF.strip()
if guardF == "":
    guardF = None

###################################################
# 検索ボタン
###################################################
if st.button("検索"):
    result = controller.filter_data(
        character1=character,
        character2=character2,
        operation=operation,
        movetype=movetype,
        command=command,
        cancel=cancel,
        zokusei=zokusei,
        startup=startup,
        hitF=hitF,
        guardF=guardF
    )
else:

    result = df

###################################################
# 表示
###################################################

display_df = result.copy()

display_df = display_df.fillna("")

display_df = display_df.astype(str)


st.dataframe(
    display_df,
    width="stretch"
)


st.write(df.dtypes)