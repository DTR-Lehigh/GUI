"""
Author       : Hanqing Qi
Date         : 2023-11-07 15:20:18
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-10 19:37:06
FilePath     : /GUI/SimpleGUI_V2/simpleGUI.py
Description  : The GUI for bicopter control V2
"""

import matplotlib.pyplot as plt
from simpleGUIutils import *
import time
import sys


class SimpleGUI:
    def __init__(self):
        # Plotting initialization
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=GUI_SIZE)
        self.ax.set_facecolor(COLORS["black"]) # Set background color
        self.fig.patch.set_facecolor(COLORS["black"]) # Set background color
        self.ax.set_xlim(0, GUI_SIZE[0])
        self.ax.set_ylim(0, GUI_SIZE[1])
        self.ax.set_aspect("equal", "box")  # Set aspect ratio
        self.ax.set_xticks([])  # Remove x ticks
        self.ax.set_yticks([])  # Remove y ticks
        self.ax.axis("off")  # Remove axis

        init_heights(self) # Heights indicator
        init_yaw(self) # Yaw indicator
        init_batterie(self) # Battery indicator

    def update(self, battery_levels:list[float] = [0]*BATTERY_NUM, heights:list[float] = [0]*HEIGHT_BAR_NUM) -> None:
        update_battery(self, battery_levels)
        update_heights(self, heights)

if __name__ == "__main__":
    mygui = SimpleGUI()
    for i in range(10):
        battery_levels = [4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2]
        heights = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        mygui.update(battery_levels, heights)
        plt.pause(0.5)
    plt.ioff()
    plt.show()

        