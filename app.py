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
st.subheader("SF6 フレームデータビューワー")

with st.expander("📖 使い方を表示"):

    st.markdown("""
#### 基本操作

① キャラクターを選択します。
② 操作タイプを選択します。
③ 「検索」を押します。
                
---
                
#### 使い方例
                
・キャラクター(比較用)を指定すると2キャラ同時に表示できます。
・キャンセル:C コマンド:↓ + 中 と検索するとモダン操作の中足ラッシュできるキャラが表示できます。
                
---
                
#### コツ
                
・コマンドは手入力でも絞込みができます。
・発生「4」で4F技だけ検索できます。
・硬直差「+4」は「4」と入力してください。
・表や列にマウスカーソルを合わせると、ソートやフルスクリーン表示ができます。
                
---
                
#### コンセプト
            
・操作キャラの変更を検討する際に、操作の類似・相違を比較したいと思い、本アプリを開発しました。
                
---
                
#### 注意事項
                
・実際のゲーム上での発生や硬直差を「正」としてください。
・WEBサイトからのデータを収集していますので、ゲームと異なる可能性があります。
---
#### 更新履歴・連絡先・その他
                
・v0.1(試作版:2026/07/12)            
・https://x.com/pome24601              
・C操作のDLCキャラはこれから1週間程かけて追加予定です。
・コマンド入力の統一性を高める修正を行います。
・誤記などは修正したいと思いますが、機能追加については基本的に対応不可となります。
""")


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
 #       key="character"
    )

    character2 = st.selectbox(
        "キャラクター(比較用)",
        controller.get_character2_list(),
#        key="character2"
    )
    operation = st.selectbox(
        "操作タイプ",
        controller.get_operation_type_list(),
#        key="operation"
    )


with col2:

    movetype = st.selectbox(
        "技タイプ",
        controller.get_movetype_type_list(),
#        key="movetype"
    )

    cancel = st.selectbox(
        "キャンセル",
        controller.get_cancel_list(),
#        key="cancel"        
    )

    zokusei = st.selectbox(
        "属性",
        controller.get_zokusei_list(),
#        key="zokusei"
    )


with col3:

    command = st.selectbox(
        "コマンド",
        controller.get_command_list(),
#        key="command"
    )

    command2 = st.selectbox(
        "コマンド(比較用)",
        controller.get_command2_list(),
#        key="command2"
    )

with col4:
    startup = st.text_input(
        "発生(数値入力)",
        value="",
#        key="startup"
    )

    startup = startup.strip()
    if startup == "":
        startup = None


    hitF = st.text_input(
        "ヒット時硬直差(数値入力)",
        value="",
#        key="hitF"
    )

    hitF = hitF.strip()
    if hitF == "":
        hitF = None


    guardF = st.text_input(
        "ガード時硬直差(数値入力)",
        value="",
#        key="guardF"
    )

    guardF = guardF.strip()
    if guardF == "":
        guardF = None


###################################################
# 検索ボタン
###################################################

search = st.button("検索")


if "result" not in st.session_state:
    st.session_state.result = df

if search:
    st.session_state.result = controller.filter_data(
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



###################################################
# 表示
###################################################

display_df = st.session_state.result.copy()

display_df = display_df.fillna("")

display_df = display_df.astype(str)

display_df = display_df.rename(columns={
    "D増加量(ヒット)": "D増加量\n(ヒット)",
    "D増加量(ガード)": "D増加量\n(ガード)",
    "D増加量(パニカン)": "D増加量\n(パニカン)",
    "ヒット時硬直差": "ヒット時\n硬直差",
    "ガード時硬直差": "ガード時\n硬直差",
})

st.dataframe(
    display_df,
    width="stretch"
)

st.write(f"検索結果：{len(st.session_state.result)}件")