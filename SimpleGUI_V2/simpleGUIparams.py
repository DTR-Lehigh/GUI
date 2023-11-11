"""
Author       : Hanqing Qi
Date         : 2023-11-10 17:40:20
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-11 14:30:50
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
FONT_SIZE = 11

# Height parameters
HEIGHT_BAR_SIZE = [0.5, 5]
HEIGHT_BAR_OFFSET = [0.25, 0, 0.25]
HEIGHT_BAR_NUM = 9
MAX_HEIGHT = 15
HEIGHT_BAR_RATIO = HEIGHT_BAR_SIZE[1] / MAX_HEIGHT
HEIGHT_BAR_HEIGHT = 2

# Yaw parameters
CIRCLE_NUM = 9
YAW_OFFSET = [0, 0.22, 0]
MAX_RADIUS = 2.4
MIN_RADIUS = MAX_RADIUS - CIRCLE_NUM * YAW_OFFSET[1]
CENTER = [7.5, 4.5]

# Battery parameters
BATTERY_NUM = 8
BATTERY_SIZE = [1.05, 0.5]
MAX_BATTERY = 4.6
BATTERY_RATIO = BATTERY_SIZE[0] / MAX_BATTERY
BATTERY_OFFSET = [0.1, 0.2, 0.1] # [left, middle, right]
BATTERY_THRESHOLD = [4, 3.7, 3.4]
BATTERY_HEIGHT = 0.5

# Distance parameters
DISTANCE_NUM = 8
DISTANCE_SIZE = [2.4, 0.5]
MAX_DISTANCE = 5
DISTANCE_RATIO = DISTANCE_SIZE[0] / MAX_DISTANCE
DISTANCE_OFFSET = [0.1, 0.2, 0.1] # [left, middle, right]
DISTANCE_THRESHOLD = [2, 1.5, 1]
DISTANCE_HEIGHT = [10.5, 11.5]