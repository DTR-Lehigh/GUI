"""
Author       : Hanqing Qi
Date         : 2023-11-11 14:47:43
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-11 15:50:36
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
        self.ax.set_aspect("equal", "box")  # Set aspect ratio
        self.ax.set_xticks([])  # Remove x ticks
        self.ax.set_yticks([])  # Remove y ticks
        self.ax.axis("off")  # Remove axis

        init_yaw(self)

    def update(self, current_yaw, desired_yaw):
        update_yaw(self, current_yaw, desired_yaw)


if __name__ == "__main__":
    mygui = SimpleGUI()
    import math

    for i in range(100):
        mygui.update(math.pi * 0.5, math.pi * 1.0)
    plt.ioff()
    plt.show()
