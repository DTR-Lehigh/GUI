"""
Author       : Hanqing Qi
Date         : 2023-11-11 14:54:50
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-11 15:36:56
FilePath     : /GUI/SimpleGUI_V3/simpleGUIparams.py
Description  : Parameters for SimpleGUI V3
"""

# Colors
C = {
    "r": "#FF5555",
    "g": "#50FA7B",
    "y": "#F1FA8C",
    "p": "#BD93F9",
    "o": "#FFB86C",
    "c": "#8BE9FD",
    "p": "#FF79C6",
    "w": "#F8F8F2",
    "k": "#282A36",
    "a": "#44475A",
    "b": "#6272A4",
}

# GUI parameters
GS = [6, 4] # GUI size
FS = 10 # Font size
LW = 1.5 # Line width

# Yaw parameters
YP = [0 * GS[0], 0 * GS[1]] # Position (left bottom corner) of yaw indicator
YS = [0.4 * GS[0], 0.4 * GS[0]] # Size of yaw indicator
YOF = [0.05 * YS[0], 0.05 * YS[1]] # Offset of yaw indicator (horizontal, vertical)
YC = [YP[0] + YS[0] / 2, YP[1] + YS[1] / 2] # Center of yaw indicator
YR = 0.4 * YS[0] # Radius of yaw indicator

# Height parameters
HEIGHT_BAR_SIZE = [0.5, 5]
HEIGHT_BAR_OFFSET = [0.25, 0, 0.25]
HEIGHT_BAR_NUM = 9
MAX_HEIGHT = 15
HEIGHT_BAR_RATIO = HEIGHT_BAR_SIZE[1] / MAX_HEIGHT
HEIGHT_BAR_HEIGHT = 2


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