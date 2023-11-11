"""
Author       : Hanqing Qi
Date         : 2023-11-08 00:15:24
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-10 19:54:27
FilePath     : /GUI/SimpleGUI_V2/simpleGUIutils.py
Description  : Some functions for the simpleGUI.py
"""

import matplotlib.widgets as widgets
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from simpleGUIparams import *
import numpy as np
import math


# Initialize the battery indicators
def init_batterie(self) -> None:
    # Battery indicator
    self.battery_indicator = []
    self.batlevel_tx = []
    for i in range(BATTERY_NUM):
        self.battery_indicator.append(self.ax.barh(BATTERY_HEIGHT + BATTERY_SIZE[1] / 2, 0, BATTERY_SIZE[1], color=None, left=BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]), zorder=1))
        self.ax.add_patch(
            patches.Rectangle(
                (BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]), BATTERY_HEIGHT), BATTERY_SIZE[0], BATTERY_SIZE[1], linewidth=1.5, edgecolor=COLORS["white"], fill=False, zorder=2
            )
        )
        self.ax.text(
            BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]) + BATTERY_SIZE[0] / 2, 1.05, f"BAT {i+1}", fontsize=FONT_SIZE, color=COLORS["white"], horizontalalignment="center", zorder=2
        )  # Battery number
        self.batlevel_tx.append(
            self.ax.text(
                BATTERY_OFFSET[0] + i * (BATTERY_SIZE[0] + BATTERY_OFFSET[1]) + BATTERY_SIZE[0] / 2,
                BATTERY_HEIGHT + BATTERY_SIZE[1] / 2,
                "?V",
                fontsize=FONT_SIZE,
                color=COLORS["white"],
                horizontalalignment="center",
                verticalalignment="center",
                zorder=3,
            )
        )  # Battery level


# Update the battery indicators
def update_battery(self, battery_levels: list[float] = [0] * BATTERY_NUM) -> None:
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
        self.battery_indicator[i][0].set_color(COLORS["white"])
        self.batlevel_tx[i].set_text("?V")


# Initialize the heights indicator
def init_heights(self) -> None:
    self.des_height_bar = None
    self.des_height_value = None
    self.cur_height_bar = []
    self.cur_height_value = []
    for i in range(HEIGHT_BAR_NUM):
        if i == 0:
            self.des_height_bar = self.ax.bar(
                HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2, 0, HEIGHT_BAR_SIZE[0], color=COLORS["red"], bottom=HEIGHT_BAR_HEIGHT, zorder=1
            )
            self.des_height_value = self.ax.text(
                HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2,
                HEIGHT_BAR_HEIGHT + 0.05,
                "0",
                fontsize=FONT_SIZE,
                color=COLORS["red"],
                horizontalalignment="center",
                verticalalignment="bottom",
                zorder=3,
            )
            self.ax.text(
                HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2,
                HEIGHT_BAR_HEIGHT - 0.1,
                "DES",
                fontsize=FONT_SIZE,
                color=COLORS["red"],
                horizontalalignment="center",
                verticalalignment="top",
                zorder=3,
            )
        else:
            self.cur_height_bar.append(
                self.ax.bar(
                    HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2, 0, HEIGHT_BAR_SIZE[0], color=COLORS["green"], bottom=HEIGHT_BAR_HEIGHT, zorder=1
                )
            )
            self.cur_height_value.append(
                self.ax.text(
                    HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2,
                    HEIGHT_BAR_HEIGHT + 0.05,
                    "0",
                    fontsize=FONT_SIZE,
                    color=COLORS["green"],
                    horizontalalignment="center",
                    verticalalignment="bottom",
                    zorder=3,
                )
            )
            self.ax.text(
                HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2,
                HEIGHT_BAR_HEIGHT - 0.1,
                f"C{i}",
                fontsize=FONT_SIZE,
                color=COLORS["green"],
                horizontalalignment="center",
                verticalalignment="top",
                zorder=3,
            )
        add_ticks_bar(self, HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]))
    # General Height Label
    self.ax.text(
        (HEIGHT_BAR_OFFSET[0] + HEIGHT_BAR_NUM * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1])) / 2,
        HEIGHT_BAR_HEIGHT + HEIGHT_BAR_SIZE[1] + 0.1,
        "Height",
        fontsize=FONT_SIZE,
        color=COLORS["white"],
        horizontalalignment="center",
        verticalalignment="bottom",
        zorder=3,
    )


# Update the heights indicator
def update_heights(self, heights: list[float] = [0] * HEIGHT_BAR_NUM) -> None:
    for i in range(0, len(heights)):
        if i == 0:
            self.des_height_bar[0].set_height((heights[i]) * HEIGHT_BAR_RATIO if (heights[i]) > 0 else 0)
            self.des_height_value.set_text(f"{(heights[i]):.2f}")
            des_height_temp = HEIGHT_BAR_HEIGHT + (heights[i]) * HEIGHT_BAR_RATIO + 0.05
            self.des_height_value.set_position((HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2, des_height_temp))
        else:
            self.cur_height_bar[i - 1][0].set_height((heights[i]) * HEIGHT_BAR_RATIO if (heights[i]) > 0 else 0)
            self.cur_height_value[i - 1].set_text(f"{(heights[i]):.2f}")
            cur_height_temp = HEIGHT_BAR_HEIGHT + (heights[i]) * HEIGHT_BAR_RATIO + 0.05
            self.cur_height_value[i - 1].set_position((HEIGHT_BAR_OFFSET[0] + i * (HEIGHT_BAR_SIZE[0] + HEIGHT_BAR_OFFSET[1]) + HEIGHT_BAR_SIZE[0] / 2, cur_height_temp))


# Add ticks to the heights indicator
def add_ticks_bar(self, left_edge: float) -> None:
    # Define how many ticks and their positions
    num_ticks = 20  # Total number of ticks
    tick_positions = np.linspace(HEIGHT_BAR_HEIGHT, HEIGHT_BAR_SIZE[1] + HEIGHT_BAR_HEIGHT, num_ticks + 1)

    for i, pos in enumerate(tick_positions):
        # Calculate the tick's start and end points
        if i == 0:
            end_x = left_edge + HEIGHT_BAR_SIZE[0]
            linewidth = 1.5  # Thicker line for the first tick
        elif i % 10 == 0:  # Long tick every 10 units
            end_x = left_edge + HEIGHT_BAR_SIZE[0] / 3
            linewidth = 1.5  # Thicker line for long ticks
        elif i % 5 == 0:  # Middle tick every 5 units
            end_x = left_edge + HEIGHT_BAR_SIZE[0] * 2 / 7
            linewidth = 1.25  # Slightly thicker line for middle ticks
        else:  # Regular tick for other units
            end_x = left_edge + HEIGHT_BAR_SIZE[0] / 7
            linewidth = 1  # Standard line width for regular ticks
        self.ax.plot([left_edge, end_x], [pos, pos], color=COLORS["white"], linewidth=linewidth, zorder=2)
    self.ax.plot([left_edge, left_edge], [HEIGHT_BAR_HEIGHT, HEIGHT_BAR_SIZE[1] + HEIGHT_BAR_HEIGHT], color=COLORS["white"], linewidth=1.5, zorder=2)


# Initialize the yaw indicator
def init_yaw(self):
    self.yaw_circles = []
    self.ax.add_patch(patches.Circle(CENTER, MAX_RADIUS, color=COLORS["white"], fill=False, linewidth=1.5, zorder=15))
    for i in range(CIRCLE_NUM):
        wedge = patches.Wedge(center=(CENTER[0], CENTER[1]), radius=MAX_RADIUS - , theta1=0, theta2=180, facecolor="blue")
        self.yaw_circles.append(wedge)
        self.ax.add_patch(wedge)

    add_ticks_circle(self)


def add_ticks_circle(self, radius: float = MAX_RADIUS) -> None:
    emphasized_angles = [0, 90, 180, 270]

    for angle in range(0, 360, 5):
        radian = np.radians(angle)
        start_x = CENTER[0] + radius * np.cos(radian)
        start_y = CENTER[1] + radius * np.sin(radian)
        if angle in emphasized_angles:
            end_x = CENTER[0] + (radius - 0.15) * np.cos(radian)
            end_y = CENTER[1] + (radius - 0.15) * np.sin(radian)
            self.ax.plot([start_x, end_x], [start_y, end_y], color=COLORS["white"], linewidth=1.5)
        else:
            end_x = CENTER[0] + (radius - 0.075) * np.cos(radian)
            end_y = CENTER[1] + (radius - 0.075) * np.sin(radian)
            self.ax.plot([start_x, end_x], [start_y, end_y], color=COLORS["white"], linewidth=1.5)
