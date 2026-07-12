import os
import tkinter as tk

from SF6_Framedata_ExcelDataManager import ExcelDataManager
from SF6_Framedata_FilterController import FilterController
from SF6_Framedata_GUI import SF6FrameDataGUI

##################################################

current_dir = os.path.dirname(__file__)

excel_path = os.path.join(
    current_dir,
    "SF6_FrameData.xlsx"
)

##################################################

excel = ExcelDataManager(excel_path)

df = excel.get_dataframe()

controller = FilterController(df)

##################################################

root = tk.Tk()

app = SF6FrameDataGUI(
    root,
    controller
)

root.mainloop()