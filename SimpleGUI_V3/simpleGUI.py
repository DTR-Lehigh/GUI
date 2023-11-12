"""
Author       : Hanqing Qi
Date         : 2023-11-11 14:47:43
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-12 14:54:57
FilePath     : /GUI/SimpleGUI_V3/simpleGUI.py
Description  : The GUI for bicopter control V3
"""

import matplotlib.pyplot as plt
from simpleGUIutils import *
import time


class SimpleGUI:
    def __init__(self):
        # Plotting initialization
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=GS)
        self.ax.set_facecolor(C["k"])  # Set background color
        self.fig.patch.set_facecolor(C["k"])  # Set background color
        self.ax.set_xlim(0, GS[0])
        self.ax.set_ylim(0, GS[1])
        self.ax.set_aspect("equal", "datalim")  # Set aspect ratio
        self.ax.set_xticks([])  # Remove x ticks
        self.ax.set_yticks([])  # Remove y ticks
        self.ax.axis("off")  # Remove axis

        init_yaw(self)
        init_height(self)
        init_variables(self)
        init_battery(self)

    def update(self):
        update_yaw(self, math.pi * 0.5,  math.pi * 2.0)
        update_height(self, 5, 11)
        update_battery(self, 4.5)


if __name__ == "__main__":
    mygui = SimpleGUI()
    import math

    for i in range(100):
        mygui.update()
    plt.ioff()
    plt.show()
