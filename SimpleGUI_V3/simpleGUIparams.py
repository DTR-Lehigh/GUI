"""
Author       : Hanqing Qi
Date         : 2023-11-11 14:54:50
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-11 18:57:59
FilePath     : /GUI/SimpleGUI_V3/simpleGUIparams.py
Description  : Parameters for SimpleGUI V3
"""

# Colors
C = {
    "r": "#fa7970", # Red
    "g": "#7ce38b", # Green
    "o": "#faa356", # Orange
    "p": "#cea5fb", # Purple
    "k": "#161b22", # Black
    "a": "#21262d", # Gray
    "w": "#ecf2f8", # White
    "c": "#a2d2fb", # Cyan
    "b": "#77bdfb", # Blue
    "y": "#c6cdd5", # Yellow
    # "i": "#FF79C6",
}

# GUI parameters
GS = [6, 4]  # GUI size
FS = 10  # Font size
LW = 1.5  # Line width

# Yaw parameters
YP = [0 * GS[0], 0 * GS[1]]  # Position (left bottom corner) of yaw indicator
YS = [0.4 * GS[0], 0.4 * GS[0]]  # Size of yaw indicator
YOF = [0.05 * YS[0], 0.05 * YS[1]]  # Offset of yaw indicator (horizontal, vertical)
YC = [YP[0] + YS[0] / 2, YP[1] + YS[1] / 2]  # Center of yaw indicator
YR = 0.4 * YS[0]  # Radius of yaw indicator

# Height parameters
HP = [0.4 * GS[0], 0]  # Position (left bottom corner) of height indicator
HS = [0.2 * GS[0], 0.4 * GS[0]]  # Size of height indicator
HOF = [0.05 * HS[0], 0.05 * HS[1]]  # Offset of height indicator (horizontal, vertical)
HW = (HS[0] - 2 * HOF[0]) / 2  # Width of height indicator
HH = HS[1] - 2 * HOF[1]
MAXH = 15  # Maximum height
HR = (HS[1] - 2 * HOF[1]) / MAXH  # Height ratio

# Variables parameters
# name, min, max, init, step, axes
NCV = 5 # Number of custom variables
V = {
    "D1": ["Yaw ", 0, 360, 0 , 1, [0.69, 0.1, 0.25, 0.05]],  # Default
    "D2": ["Height ", 0, 15, 0, 0.1, [0.69, 0.17, 0.25, 0.05]],  # Default
    "P1": ["force x ", 0, 1, 0, 0.01, [0.69, 0.24, 0.25, 0.05]],  # P1 (Force_x)
    "P2": ["z level ", 1, 3, 1, 1, [0.69, 0.31, 0.25, 0.05]],  # P2 (z_level)
    "P3": ["t rotate ", 0, 10, 0, 0.01, [0.69, 0.38, 0.25, 0.05]],  # P3 (time_rotate)
    "P4": ["angle ", -90, 90, 0, 0.2, [0.69, 0.45, 0.25, 0.05]],  # P4 (angle)
    "P5": ["zigzag ", 0, 15, 5, 1, [0.69, 0.52, 0.25, 0.05]],  # P5 (zigzag)
}


# Battery parameters
BATTERY_NUM = 8
BATTERY_SIZE = [1.05, 0.5]
MAX_BATTERY = 4.6
BATTERY_RATIO = BATTERY_SIZE[0] / MAX_BATTERY
BATTERY_OFFSET = [0.1, 0.2, 0.1]  # [left, middle, right]
BATTERY_THRESHOLD = [4, 3.7, 3.4]
BATTERY_HEIGHT = 0.5

# Distance parameters
DISTANCE_NUM = 8
DISTANCE_SIZE = [2.4, 0.5]
MAX_DISTANCE = 5
DISTANCE_RATIO = DISTANCE_SIZE[0] / MAX_DISTANCE
DISTANCE_OFFSET = [0.1, 0.2, 0.1]  # [left, middle, right]
DISTANCE_THRESHOLD = [2, 1.5, 1]
DISTANCE_HEIGHT = [10.5, 11.5]
