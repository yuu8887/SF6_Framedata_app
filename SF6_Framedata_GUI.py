import tkinter as tk
from tkinter import ttk
import pandas as pd


class SF6FrameDataGUI:

    def __init__(self, root, controller):

        self.root = root
        self.controller = controller

        root.title("SF6技情報一覧")
        root.geometry("900x600")

        ##################################################
        # 検索条件
        ##################################################

        condition_frame = ttk.LabelFrame(
            root,
            text="検索条件"
        )

        condition_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # キャラ名1
        ttk.Label(
            condition_frame,
            text="キャラクター1"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.character1_combo = ttk.Combobox(
            condition_frame,
            state="readonly",
            width=20
        )

        self.character1_combo["values"] = controller.get_character1_list()

        self.character1_combo.current(0)

        self.character1_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # キャラ名2
        ttk.Label(
            condition_frame,
            text="キャラクター2"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.character2_combo = ttk.Combobox(
            condition_frame,
            state="readonly",
            width=20
        )

        self.character2_combo["values"] = controller.get_character2_list()

        self.character2_combo.current(0)

        self.character2_combo.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )


        # 操作タイプ
        ttk.Label(
         condition_frame,
         text="操作タイプ"
        ).grid(row=2, column=0, padx=5, pady=5)

        self.operation_combo = ttk.Combobox(
            condition_frame,
         state="readonly",
         width=20
        )

        self.operation_combo["values"] = controller.get_operation_type_list()

        self.operation_combo.current(0)

        self.operation_combo.grid(
          row=2,
           column=1,
           padx=5,
           pady=5
        )

        # 技タイプ
        ttk.Label(
         condition_frame,
         text="技タイプ"
        ).grid(row=3, column=0, padx=5, pady=5)

        self.movetype_combo = ttk.Combobox(
            condition_frame,
         state="readonly",
         width=20
        )

        self.movetype_combo["values"] = controller.get_movetype_type_list()

        self.movetype_combo.current(0)

        self.movetype_combo.grid(
          row=3,
           column=1,
           padx=5,
           pady=5
        )


        # コマンド
        ttk.Label(
         condition_frame,
         text="コマンド"
        ).grid(row=4, column=0, padx=5, pady=5)

        self.command_combo = ttk.Combobox(
            condition_frame,
         state="readonly",
         width=20
        )

        self.command_combo["values"] = controller.get_command_list()

        self.command_combo.current(0)

        self.command_combo.grid(
          row=4,
           column=1,
           padx=5,
           pady=5
        )


        # キャンセル
        ttk.Label(
         condition_frame,
         text="キャンセル"
        ).grid(row=0, column=2, padx=5, pady=5)

        self.cancel_combo = ttk.Combobox(
            condition_frame,
         state="readonly",
         width=20
        )

        self.cancel_combo["values"] = controller.get_cancel_list()

        self.cancel_combo.current(0)

        self.cancel_combo.grid(
          row=0,
           column=3,
           padx=5,
           pady=5
        )


        # 発生
        ttk.Label(
            condition_frame,
            text="発生(数値入力)"
        ).grid(row=1, column=2, padx=5, pady=5)

        self.startup_entry = ttk.Entry(
            condition_frame,
            width=10
        )

        self.startup_entry.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        # ヒット時硬直差
        ttk.Label(
            condition_frame,
            text="H硬直差(数値orD)"
        ).grid(row=2, column=2, padx=5, pady=5)

        self.hitF_entry = ttk.Entry(
            condition_frame,
            width=10
        )

        self.hitF_entry.grid(
            row=2,
            column=3,
            padx=5,
            pady=5
        )

        # ガード時硬直差
        ttk.Label(
            condition_frame,
            text="G硬直差(数値)"
        ).grid(row=3, column=2, padx=5, pady=5)

        self.guardF_entry = ttk.Entry(
            condition_frame,
            width=10
        )

        self.guardF_entry.grid(
            row=3,
            column=3,
            padx=5,
            pady=5
        )

        # 属性
        ttk.Label(
         condition_frame,
         text="属性"
        ).grid(row=4, column=2, padx=5, pady=5)

        self.zokusei_combo = ttk.Combobox(
            condition_frame,
         state="readonly",
         width=20
        )

        self.zokusei_combo["values"] = controller.get_zokusei_list()

        self.zokusei_combo.current(0)

        self.zokusei_combo.grid(
          row=4,
           column=3,
           padx=5,
           pady=5
        )


        ##################################################
        # ボタン
        ##################################################

        search_button = ttk.Button(
            condition_frame,
            text="結果を表示",
            command=self.search
        )

        search_button.grid(
            row=0,
            column=5,
            padx=20
        )

        ##################################################
        # 結果表示
        ##################################################

        self.tree = ttk.Treeview(root)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.show_dataframe(
            controller.df
        )

    ##################################################

    def show_dataframe(self, dataframe):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(dataframe.columns)

        self.tree["show"] = "headings"

        for col in dataframe.columns:

            self.tree.heading(col, text=col)

            self.tree.column(
                col,
                width=90,
                anchor="center"
            )

        for _, row in dataframe.iterrows():

            values = [
            self.format_value(v)
            for v in row
            ]

            self.tree.insert(
                "",
                "end",
                values=values
            )

    ##################################################

    def search(self):

        character1 = self.character1_combo.get()
        character2 = self.character2_combo.get()
        operation = self.operation_combo.get()
        movetype = self.movetype_combo.get()
        command = self.command_combo.get()
        cancel = self.cancel_combo.get()
        startup_text = self.startup_entry.get()
        hitF_text = self.hitF_entry.get()
        guardF_text = self.guardF_entry.get()
        zokusei = self.zokusei_combo.get()

        if startup_text == "":
            startup = None
        else:
            startup = int(startup_text)

        if hitF_text == "":
            hitF = None
        else:
            hitF = hitF_text

        if guardF_text == "":
            guardF = None
        else:
            guardF = int(guardF_text)

        result = self.controller.filter_data(
            character1=character1,
            character2=character2,
            operation=operation,
            movetype=movetype,
            command=command,
            cancel=cancel,
            startup=startup,
            hitF=hitF,
            guardF=guardF,
            zokusei=zokusei
        )

        self.show_dataframe(result)

    def format_value(self, value):

        if pd.isna(value):
            return ""

        if isinstance(value, float):

            if value.is_integer():
                return str(int(value))

        return str(value)

