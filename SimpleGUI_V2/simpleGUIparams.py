"""
Author       : Hanqing Qi
Date         : 2023-11-10 17:40:20
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-10 18:34:45
FilePath     : /GUI/SimpleGUI_V2/simpleGUIparams.py
Description  : Parameters for the simpleGUI.py
"""

# Colors
COLORS = {
    "red": "#FF5555",
    "green": "#50FA7B",
    "yellow": "#F1FA8C",
    "purple": "#BD93F9",
    "orange": "#FFB86C",
    "cyan": "#8BE9FD",
    "pink": "#FF79C6",
    "white": "#F8F8F2",
    "black": "#282A36",
    "gray": "#44475A",
    "drak_blue": "#6272A4",
}

# GUI parameters
GUI_SIZE = [10, 10]
FONT_SIZE = 10

# Battery parameters
BATTERY_NUM = 8
BATTERY_SIZE = [1.05, 0.5]
MAX_BATTERY = 4.6
BATTERY_RATIO = BATTERY_SIZE[0] / MAX_BATTERY
BATTERY_OFFSET = [0.1, 0.2, 0.1] # [left, middle, right]
BATTERY_THRESHOLD = [4, 3.7, 3.4]