"""
Author       : Hanqing Qi
Date         : 2023-11-08 00:15:24
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-10 18:32:44
FilePath     : /GUI/SimpleGUI_V2/simpleGUIutils.py
Description  : Some functions for the simpleGUI.py
"""

import matplotlib.widgets as widgets
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from simpleGUIparams import *
import numpy as np
import math


def init_batterie(self)->None:
    # Battery indicator
    self.battery_indicator = []
    self.batlevel_tx = []
    for i in range(BATTERY_NUM):
        self.battery_indicator.append(self.ax.barh(0.5 + BATTERY_SIZE[1]/2, 0, BATTERY_SIZE[1], color=None, left=BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]), zorder=2))
        print(self.battery_indicator[i])
        self.ax.add_patch(
            patches.Rectangle((BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]), 0.5), BATTERY_SIZE[0], BATTERY_SIZE[1], linewidth=1, edgecolor=None, facecolor=COLORS["gray"], zorder=1)
        )
        self.ax.text(
            BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]) + BATTERY_SIZE[0] / 2, 1.05, f"BAT {i+1}", fontsize=FONT_SIZE, color=COLORS["white"], horizontalalignment="center", zorder=3
        )  # Battery number
        self.batlevel_tx.append(
            self.ax.text(
                BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]) + BATTERY_SIZE[0] / 2,
                0.5 + BATTERY_SIZE[1] / 2,
                "?V",
                fontsize=FONT_SIZE,
                color=COLORS["white"],
                horizontalalignment="center",
                verticalalignment="center",
                zorder=3,
            )
        )  # Battery level
    
def update_battery(self, battery_levels:list[float] = [0]*BATTERY_NUM)->None:
    for i in range(len(battery_levels)):
        current_battery_level = min(battery_levels[i], MAX_BATTERY)
        self.battery_indicator[i][0].set_width(current_battery_level * BATTERY_RATIO if current_battery_level >= 0 else 0)
        if current_battery_level > BATTERY_THRESHOLD[0]:
            self.battery_indicator[i][0].set_color(COLORS["green"])
        elif current_battery_level > BATTERY_THRESHOLD[1]:
            self.battery_indicator[i][0].set_color(COLORS["yellow"])
        elif current_battery_level > BATTERY_THRESHOLD[2]:
            self.battery_indicator[i][0].set_color(COLORS["orange"])
        else:
            self.battery_indicator[i][0].set_color(COLORS["red"])
        self.batlevel_tx[i].set_color(COLORS["black"])
        self.batlevel_tx[i].set_text(f"{(current_battery_level):.2f}V")
    for i in range(len(battery_levels), BATTERY_NUM):
        self.battery_indicator[i][0].set_width(0)
        self.batlevel_tx[i].set_text("?V")
