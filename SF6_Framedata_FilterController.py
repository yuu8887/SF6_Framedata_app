class FilterController:

    def __init__(self, dataframe):
        self.df = dataframe

    def filter_data(
            self,
            character1="すべて",
            character2="指定なし",
            operation="すべて",
            movetype="すべて",
            command="すべて",
            cancel="すべて",
            startup=None,
            hitF=None,
            guardF=None,
            zokusei="すべて"):

        result = self.df.copy()

        if character1 != "すべて":

            character_list = []
            # キャラクター①
            if character1 != "指定なし":
                character_list.append(character1)

            # キャラクター②
            if character2 != "指定なし":
                if character2 not in character_list:
                    character_list.append(character2)

            result = result[result["キャラ名"].isin(character_list)]

        if operation != "すべて":
            result = result[result["操作タイプ"] == operation]

        if movetype != "すべて":
            result = result[result["技タイプ"] == movetype]

        if command != "すべて":
            result = result[result["コマンド"] == command]

        if cancel != "すべて":
            result = result[result["キャンセル"] == cancel]

        if startup is not None:
            result = result[result["発生"] == startup]

        if hitF is not None:
            result = result[result["ヒット時硬直差"].astype(str) == hitF]

        if guardF is not None:
            result = result[result["ガード時硬直差"] == guardF]

        if zokusei != "すべて":
            result = result[result["属性"] == zokusei]

        return result

    def get_character1_list(self):

        character_list = sorted(
            self.df["キャラ名"].dropna().unique().tolist()
        )

        character_list.insert(0, "すべて")

        return character_list
    
    def get_character2_list(self):

        character_list = sorted(
            self.df["キャラ名"].dropna().unique().tolist()
        )

        character_list.insert(0, "指定なし")

        return character_list
    
    def get_operation_type_list(self):

        operation_list = sorted(
            self.df["操作タイプ"].dropna().unique().tolist()
        )

        operation_list.insert(0, "すべて")

        return operation_list
    
    def get_movetype_type_list(self):

        movetype_list = sorted(
            self.df["技タイプ"].dropna().unique().tolist()
        )

        movetype_list.insert(0, "すべて")

        return movetype_list

    def get_command_list(self):

        command_list = sorted(
            self.df["コマンド"].dropna().unique().tolist()
        )

        command_list.insert(0, "すべて")

        return command_list
    
    def get_cancel_list(self):

        cancel_list = sorted(
            self.df["キャンセル"].dropna().unique().tolist()
        )

        cancel_list.insert(0, "すべて")

        return cancel_list
    
    def get_startup_list(self):

        startup_list = sorted(
            self.df["発生"].dropna().unique().tolist()
        )

        startup_list.insert(0, "すべて")

        return startup_list
    
    def get_hitF_list(self):

        hitF_list = sorted(
            self.df["ヒット時硬直差"].dropna().unique().tolist()
        )

        hitF_list.insert(0, "すべて")

        return hitF_list
    
    def get_guardF_list(self):

        guardF_list = sorted(
            self.df["ガード時硬直差"].dropna().unique().tolist()
        )

        guardF_list.insert(0, "すべて")

        return guardF_list
    
    def get_zokusei_list(self):

        zokusei_list = sorted(
            self.df["属性"].dropna().unique().tolist()
        )

        zokusei_list.insert(0, "すべて")

        return zokusei_list