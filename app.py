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

st.set_page_config(
    page_title="SF6 フレームデータビューワー",
    layout="wide"
)

###################################################
# キャラクター選択
###################################################

col1, col2, col3, col4 = st.columns(4)

with col1:

    character = st.selectbox(
        "キャラクター",
        controller.get_character1_list(),
        key="character"
    )

    character2 = st.selectbox(
        "キャラクター(比較用)",
        controller.get_character2_list(),
        key="character2"
    )
    operation = st.selectbox(
        "操作タイプ",
        controller.get_operation_type_list(),
        key="operation"
    )


with col2:

    movetype = st.selectbox(
        "技タイプ",
        controller.get_movetype_type_list(),
        key="movetype"
    )

    cancel = st.selectbox(
        "キャンセル",
        controller.get_cancel_list(),
        
    )

    zokusei = st.selectbox(
        "属性",
        controller.get_zokusei_list(),
        key="zokusei"
    )


with col3:

    command = st.selectbox(
        "コマンド",
        controller.get_command_list(),
        key="command"
    )

    command2 = st.selectbox(
        "コマンド(比較用)",
        controller.get_command2_list(),
        key="command2"
    )

with col4:
    startup = st.text_input(
        "発生(数値入力)",
        value="",
        key="startup"
    )

    startup = startup.strip()
    if startup == "":
        startup = None


    hitF = st.text_input(
        "ヒット時硬直差(数値入力)",
        value="",
        key="hitF"
    )

    hitF = hitF.strip()
    if hitF == "":
        hitF = None


    guardF = st.text_input(
        "ガード時硬直差(数値入力)",
        value="",
        key="guardF"
    )

    guardF = guardF.strip()
    if guardF == "":
        guardF = None


###################################################
# 検索ボタン
###################################################
col1, col2 = st.columns(2)

with col1:
    search = st.button("検索")

with col2:
    clear = st.button("クリア")

if search:
    result = controller.filter_data(
        character1=character,
        character2=character2,
        operation=operation,
        movetype=movetype,
        command=command,
        command2=command2,
        cancel=cancel,
        zokusei=zokusei,
        startup=startup,
        hitF=hitF,
        guardF=guardF
    )
else:

    result = df

if clear:

    st.session_state.character = "すべて"
    st.session_state.character2 = "指定なし"

    st.session_state.operation = "すべて"
    st.session_state.movetype = "すべて"
    st.session_state.command = "すべて"
    st.session_state.cancel = "すべて"
    st.session_state.zokusei = "すべて"

    st.session_state.startup = ""
    st.session_state.hitF = ""
    st.session_state.guardF = ""

    st.rerun()

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

st.write(f"検索結果：{len(result)}件")