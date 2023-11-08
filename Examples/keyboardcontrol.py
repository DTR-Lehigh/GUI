"""
Author       : Hanqing Qi
Date         : 2023-11-07 15:19:42
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-07 18:44:18
FilePath     : /GUI/keyboardcontrol.py
Description  : Class to use pygame to get keyboard inputs for GUI
"""
import pygame
import time

# Macros
G_YAW = 0.1
G_HEIGHT = 0.07
G_WALLSENSOR = 0.1
G_ROI = 0.1
G_BAT = 1
FRAME = [0, 0, 240, 160]

class KeyboardControl:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((100, 100))
        self.des_yaw = 0
        self.des_height = 0
        self.wall_sensor = 0
        self.batlevel = 0
        self.roi = [0, 0, 0, 0]
        self.connection = 0
        self.running = True

    def get_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.des_height += G_HEIGHT # Increase height
        if keys[pygame.K_DOWN]:
            self.des_height -= G_HEIGHT # Decrease height
        if keys[pygame.K_LEFT]:
            self.des_yaw += G_YAW # Turn left
        if keys[pygame.K_RIGHT]: 
            self.des_yaw -= G_YAW # Turn right
        if keys[pygame.K_w]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: 
                self.roi[2] += G_ROI # Increase ROI width
            else:
                self.roi[0] += G_ROI # Increase ROI position x
        if keys[pygame.K_s]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.roi[2] -= G_ROI # Decrease ROI width 
            else:
                self.roi[0] -= G_ROI # Decrease ROI position x
        if keys[pygame.K_a]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.roi[3] += G_ROI # Increase ROI height
            else:
                self.roi[1] += G_ROI # Increase ROI position y
        if keys[pygame.K_d]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.roi[3] -= G_ROI # Decrease ROI height
            else:
                self.roi[1] -= G_ROI # Decrease ROI position y
        # Clamp ROI values
        for vals in self.roi:
            vals = max(min(vals, 240), 0)
        if keys[pygame.K_SPACE]:
            self.connection = 0 # Disconnect
        else:
            self.connection = 1
        if keys[pygame.K_b]:
            self.batlevel += G_BAT
        else:
            self.batlevel -= 0.01
        if keys[pygame.K_EQUALS]:
            self.wall_sensor += G_WALLSENSOR
        if keys[pygame.K_MINUS]:
            self.wall_sensor -= G_WALLSENSOR
        if keys[pygame.K_ESCAPE]:
            self.running = False

        # Now round the values to two decimal places
        self.des_yaw = round(self.des_yaw, 2)
        self.des_height = round(self.des_height, 2)
        self.wall_sensor = round(self.wall_sensor, 2)
        self.roi = [round(value, 2) for value in self.roi]
        self.batlevel = round(self.batlevel, 2)

        print(self.des_yaw, self.des_height, self.wall_sensor, self.roi, self.batlevel, self.connection)
        return self.des_yaw, self.des_height, self.wall_sensor, self.roi, self.batlevel, self.connection

    def is_running(self):
        return self.running

    def shutdown(self):
        pygame.quit()

if __name__ == "__main__":
    keyboard = KeyboardControl()
    while keyboard.is_running():
        keyboard.get_inputs()
        time.sleep(0.1)
    keyboard.shutdown()
