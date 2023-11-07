"""
Author       : Hanqing Qi
Date         : 2023-11-07 14:19:23
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-07 14:29:57
FilePath     : /GUI/Examples/tkinter_test.py
Description  : A simple example of a progress bar in Tkinter
"""

import tkinter as tk
import time

def update_bar(value):
    # Ensure that the bottom of the bar stays at y=150 and adjust the top according to the value
    canvas.coords(bar, (10, 150, 10 + 20, 150 - value))

root = tk.Tk()
root.title("Value Bar")

canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

# Create a bar. The coordinates are (x1, y1, x2, y2).
bar = canvas.create_rectangle(10, 150, 30, 150, fill="blue")

# Function to animate the bar rising and falling
def animate_bar():
    for i in range(0, 140, 10):  # Rise
        update_bar(i)
        root.update()
        time.sleep(0.1)
    for i in range(140, -10, -10):  # Fall
        update_bar(i)
        root.update()
        time.sleep(0.1)

# Run the animation in a loop
while True:
    animate_bar()

root.mainloop()
